#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TIER_RULES = {
    "earnings release": ("A", "Confirmed"),
    "earnings call": ("A", "Confirmed"),
    "official product page": ("A", "Confirmed"),
    "investor presentation": ("A", "Confirmed"),
    "company press release": ("A", "Confirmed"),
    "industry article": ("B", "Inferred"),
    "conference summary": ("B", "Inferred"),
    "sell-side summary": ("B", "Inferred"),
    "tweet": ("C", "Weak"),
    "forum": ("C", "Weak"),
}

SIGNAL_PATTERNS = [
    (r"\b(demand|demanded|demanding)\b", "demand"),
    (r"\b(hbm)\b", "HBM"),
    (r"\b(ai)\b", "AI"),
    (r"\b(packaging|advanced packaging|hybrid bonding)\b", "advanced packaging"),
    (r"\b(test|probe|inspection|yield|metrology)\b", "test and inspection"),
    (r"\b(expansion|expand|ramp|production)\b", "ramp"),
    (r"\b(liquid cooling|cooling|power)\b", "power and cooling"),
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def normalize_source_type(source_type: str) -> tuple[str, str]:
    key = source_type.strip().lower()
    return TIER_RULES.get(key, ("D", "Needs verification"))


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return slug or "item"


def summarize_body(body: str, max_chars: int = 220) -> str:
    text = " ".join(body.split())
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars].rsplit(" ", 1)[0].strip()
    return cut + "..."


def extract_signals(text: str) -> list[str]:
    found = []
    lower = text.lower()
    for pattern, label in SIGNAL_PATTERNS:
        if re.search(pattern, lower):
            found.append(label)
    return sorted(set(found))


def infer_evidence_score(label: str) -> int:
    return {"Confirmed": 5, "Inferred": 4, "Weak": 2, "Needs verification": 1}.get(label, 1)


def infer_catalyst_score(signals: list[str]) -> int:
    if "ramp" in signals or "advanced packaging" in signals:
        return 4
    if "power and cooling" in signals:
        return 4
    if signals:
        return 3
    return 2


def infer_constraint_score(company: dict, aggregated_signals: list[str]) -> int:
    if "constraint_hint" in company:
        return int(company["constraint_hint"])
    if "HBM" in aggregated_signals or "advanced packaging" in aggregated_signals:
        return 4
    if "power and cooling" in aggregated_signals:
        return 4
    return 3


def build_evidence_records(sources: list[dict]) -> tuple[list[dict], dict]:
    evidence = []
    entity_signals: dict[str, set[str]] = {}
    for idx, source in enumerate(sources, start=1):
        tier, label = normalize_source_type(source["source_type"])
        summary = summarize_body(source["body"])
        signals = extract_signals(source["title"] + " " + source["body"])
        entity_signals.setdefault(source["entity"], set()).update(signals)
        evidence.append(
            {
                "id": f"ev_{slugify(source['entity'])}_{idx}",
                "tier": tier,
                "label": label,
                "source_type": source["source_type"],
                "entity": source["entity"],
                "title": source["title"],
                "summary": summary,
                "url": source["url"],
                "signals": signals,
            }
        )
    entity_signals = {k: sorted(v) for k, v in entity_signals.items()}
    return evidence, entity_signals


def build_company_records(companies: list[dict], entity_signals: dict[str, list[str]]) -> list[dict]:
    out = []
    for company in companies:
        signals = entity_signals.get(company["name"], [])
        evidence_score = infer_evidence_score("Confirmed") if signals else 3
        catalyst_score = infer_catalyst_score(signals)
        out.append(
            {
                "ticker": company["ticker"],
                "name": company["name"],
                "role": company["role"],
                "stack_layer": company["stack_layer"],
                "market_cap_usd_b": company["market_cap_usd_b"],
                "constraint_score": infer_constraint_score(company, signals),
                "evidence_score": evidence_score,
                "consensus_score": int(company.get("consensus_hint", 3)),
                "mispricing_score": int(company.get("mispricing_hint", 3)),
                "catalyst_score": catalyst_score,
                "risk": company["risk"],
                "notes": f"Signals: {', '.join(signals) if signals else 'no extracted signals'}",
            }
        )
    return out


def build_catalysts(entity_signals: dict[str, list[str]]) -> list[dict]:
    labels = []
    combined = sorted({signal for signals in entity_signals.values() for signal in signals})
    if "advanced packaging" in combined or "HBM" in combined:
        labels.append(
            {
                "label": "Packaging and HBM updates",
                "type": "earnings / capex",
                "watch_for": "Ramps, production language, and sustained AI packaging demand",
            }
        )
    if "power and cooling" in combined:
        labels.append(
            {
                "label": "Power and cooling deployment updates",
                "type": "deployment",
                "watch_for": "Faster site readiness, power density upgrades, and liquid-cooling rollout",
            }
        )
    if not labels:
        labels.append(
            {
                "label": "Next earnings cycle",
                "type": "earnings",
                "watch_for": "Whether management language confirms or weakens the thesis",
            }
        )
    return labels


def build_draft_pack(payload: dict) -> tuple[dict, dict]:
    evidence, entity_signals = build_evidence_records(payload.get("sources", []))
    companies = build_company_records(payload.get("companies", []), entity_signals)
    catalysts = build_catalysts(entity_signals)

    draft_pack = {
        "meta": payload["meta"],
        "thesis": payload["thesis"],
        "stack_layers": payload["stack_layers"],
        "bottlenecks": payload["bottlenecks"],
        "evidence": evidence,
        "companies": companies,
        "catalysts": catalysts,
    }

    extraction_report = {
        "meta": payload["meta"],
        "source_count": len(payload.get("sources", [])),
        "evidence_count": len(evidence),
        "companies_count": len(companies),
        "entity_signals": entity_signals,
    }

    return draft_pack, extraction_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Turn a source bundle into a draft Chokepoint Atlas pack input.")
    parser.add_argument("--input", required=True, help="Path to a JSON source bundle")
    parser.add_argument("--output", required=True, help="Output directory for extracted draft files")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    ensure_dir(output_dir)

    payload = load_json(input_path)
    draft_pack, extraction_report = build_draft_pack(payload)

    write_json(output_dir / "draft_pack_input.json", draft_pack)
    write_json(output_dir / "extraction_report.json", extraction_report)

    print(f"Built draft pack input at: {output_dir}")


if __name__ == "__main__":
    main()
