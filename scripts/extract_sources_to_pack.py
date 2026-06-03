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

CONFIDENCE_BY_LABEL = {
    "Confirmed": "High",
    "Inferred": "Medium",
    "Weak": "Low",
    "Needs verification": "Very low",
}


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


def split_sentences(text: str) -> list[str]:
    cleaned = " ".join(text.split())
    if not cleaned:
        return []
    parts = re.split(r"(?<=[\.\!\?])\s+", cleaned)
    return [part.strip() for part in parts if part.strip()]


def extract_signals(text: str) -> list[str]:
    found = []
    lower = text.lower()
    for pattern, label in SIGNAL_PATTERNS:
        if re.search(pattern, lower):
            found.append(label)
    return sorted(set(found))


def extract_quote_snippets(body: str, signals: list[str], max_snippets: int = 2, max_chars: int = 180) -> list[str]:
    sentences = split_sentences(body)
    if not sentences:
        return []

    selected: list[str] = []
    signal_terms = {signal.lower() for signal in signals}

    for sentence in sentences:
        lower = sentence.lower()
        if any(term in lower for term in signal_terms):
            selected.append(sentence)
        if len(selected) >= max_snippets:
            break

    if not selected:
        selected = sentences[:max_snippets]

    trimmed = []
    for sentence in selected:
        if len(sentence) <= max_chars:
            trimmed.append(sentence)
        else:
            trimmed.append(sentence[:max_chars].rsplit(" ", 1)[0].strip() + "...")
    return trimmed


def build_link_reason(entity: str, signals: list[str], company_role: str | None = None) -> str:
    if company_role and signals:
        return f"{entity} is linked because the source directly mentions {', '.join(signals[:3])}, which supports its role as {company_role}."
    if signals:
        return f"{entity} is linked because the source explicitly points to {', '.join(signals[:3])}."
    if company_role:
        return f"{entity} is linked because the source is a primary-source mention relevant to its role as {company_role}."
    return f"{entity} is linked because the source is directly relevant to the current lane."


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


def infer_evidence_score_from_records(entity_records: list[dict]) -> int:
    if not entity_records:
        return 3
    score_map = {"High": 5, "Medium": 4, "Low": 2, "Very low": 1}
    values = [score_map.get(record.get("source_confidence", "Medium"), 3) for record in entity_records]
    return max(round(sum(values) / len(values)), 1)


def build_evidence_records(sources: list[dict], companies: list[dict] | None = None) -> tuple[list[dict], dict, dict]:
    evidence = []
    entity_signals: dict[str, set[str]] = {}
    entity_records: dict[str, list[dict]] = {}
    company_roles = {company["name"]: company.get("role") for company in (companies or [])}
    for idx, source in enumerate(sources, start=1):
        tier, label = normalize_source_type(source["source_type"])
        summary = summarize_body(source["body"])
        signals = extract_signals(source["title"] + " " + source["body"])
        snippets = extract_quote_snippets(source["body"], signals)
        source_confidence = CONFIDENCE_BY_LABEL[label]
        link_reason = build_link_reason(source["entity"], signals, company_roles.get(source["entity"]))
        entity_signals.setdefault(source["entity"], set()).update(signals)
        record = {
            "id": f"ev_{slugify(source['entity'])}_{idx}",
            "tier": tier,
            "label": label,
            "source_type": source["source_type"],
            "entity": source["entity"],
            "title": source["title"],
            "summary": summary,
            "url": source["url"],
            "signals": signals,
            "quote_snippets": snippets,
            "source_confidence": source_confidence,
            "link_reason": link_reason,
        }
        evidence.append(record)
        entity_records.setdefault(source["entity"], []).append(record)
    entity_signals = {k: sorted(v) for k, v in entity_signals.items()}
    return evidence, entity_signals, entity_records


def build_company_records(companies: list[dict], entity_signals: dict[str, list[str]], entity_records: dict[str, list[dict]]) -> list[dict]:
    out = []
    for company in companies:
        signals = entity_signals.get(company["name"], [])
        records = entity_records.get(company["name"], [])
        evidence_score = infer_evidence_score_from_records(records)
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
                "source_confidence": records[0]["source_confidence"] if records else "Medium",
                "evidence_count": len(records),
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
    evidence, entity_signals, entity_records = build_evidence_records(payload.get("sources", []), payload.get("companies", []))
    companies = build_company_records(payload.get("companies", []), entity_signals, entity_records)
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
        "quote_coverage": {
            record["id"]: len(record.get("quote_snippets", [])) for record in evidence
        },
        "entity_confidence": {
            entity: records[0]["source_confidence"] if records else "Medium"
            for entity, records in entity_records.items()
        },
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
