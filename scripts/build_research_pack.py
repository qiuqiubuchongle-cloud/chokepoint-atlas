#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


EVIDENCE_ORDER = {"Confirmed": 4, "Inferred": 3, "Weak": 2, "Needs verification": 1}
TIER_TO_LABEL = {"A": "Confirmed", "B": "Inferred", "C": "Weak", "D": "Needs verification"}
SCORE_FIELDS = [
    "constraint_score",
    "evidence_score",
    "consensus_score",
    "mispricing_score",
    "catalyst_score",
]
REQUIRED_TOP_LEVEL = ["meta", "thesis", "stack_layers", "bottlenecks", "evidence", "companies", "catalysts"]
REQUIRED_META_FIELDS = ["pack_id", "title", "as_of_date"]
REQUIRED_THESIS_FIELDS = [
    "supertrend",
    "end_system",
    "lane",
    "thesis_sentence",
    "bottleneck_call",
    "weakest_assumption",
    "thesis_breaker",
]
REQUIRED_COMPANY_FIELDS = ["ticker", "name", "role", "stack_layer", "market_cap_usd_b", "risk", *SCORE_FIELDS]
REQUIRED_EVIDENCE_FIELDS = ["id", "tier", "entity", "title", "summary", "url"]
REQUIRED_CATALYST_FIELDS = ["label", "type", "watch_for"]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def collect_missing_fields(payload: dict, required_fields: list[str], prefix: str) -> list[str]:
    issues = []
    for field in required_fields:
        if field not in payload or payload[field] in (None, "", []):
            issues.append(f"{prefix}.{field} is required")
    return issues


def validate_score(field_name: str, value: object, prefix: str) -> list[str]:
    issues = []
    if not isinstance(value, (int, float)):
        return [f"{prefix}.{field_name} must be a number"]
    if value < 1 or value > 5:
        issues.append(f"{prefix}.{field_name} must be between 1 and 5")
    return issues


def validate_input(data: dict) -> dict:
    issues: list[str] = []

    for field in REQUIRED_TOP_LEVEL:
        if field not in data:
            issues.append(f"top-level field `{field}` is required")

    if issues:
        raise ValueError("Invalid research pack input:\n- " + "\n- ".join(issues))

    issues.extend(collect_missing_fields(data["meta"], REQUIRED_META_FIELDS, "meta"))
    issues.extend(collect_missing_fields(data["thesis"], REQUIRED_THESIS_FIELDS, "thesis"))

    stack_layers = data.get("stack_layers", [])
    if not isinstance(stack_layers, list) or not stack_layers:
        issues.append("stack_layers must be a non-empty list")
    layer_ids = set()
    for idx, layer in enumerate(stack_layers):
        prefix = f"stack_layers[{idx}]"
        issues.extend(collect_missing_fields(layer, ["id", "label", "items"], prefix))
        if isinstance(layer, dict) and layer.get("id") in layer_ids:
            issues.append(f"{prefix}.id must be unique")
        if isinstance(layer, dict) and layer.get("id"):
            layer_ids.add(layer["id"])

    companies = data.get("companies", [])
    if not isinstance(companies, list) or not companies:
        issues.append("companies must be a non-empty list")
    for idx, company in enumerate(companies):
        prefix = f"companies[{idx}]"
        issues.extend(collect_missing_fields(company, REQUIRED_COMPANY_FIELDS, prefix))
        if company.get("stack_layer") and company["stack_layer"] not in layer_ids:
            issues.append(f"{prefix}.stack_layer must reference an existing stack layer id")
        if isinstance(company.get("market_cap_usd_b"), (int, float)) and company["market_cap_usd_b"] <= 0:
            issues.append(f"{prefix}.market_cap_usd_b must be > 0")
        for field_name in SCORE_FIELDS:
            if field_name in company:
                issues.extend(validate_score(field_name, company[field_name], prefix))

    evidence = data.get("evidence", [])
    if not isinstance(evidence, list) or not evidence:
        issues.append("evidence must be a non-empty list")
    evidence_ids = set()
    for idx, record in enumerate(evidence):
        prefix = f"evidence[{idx}]"
        issues.extend(collect_missing_fields(record, REQUIRED_EVIDENCE_FIELDS, prefix))
        if record.get("id") in evidence_ids:
            issues.append(f"{prefix}.id must be unique")
        if record.get("id"):
            evidence_ids.add(record["id"])
        tier = str(record.get("tier", "")).upper()
        if tier and tier not in TIER_TO_LABEL:
            issues.append(f"{prefix}.tier must be one of A/B/C/D")

    catalysts = data.get("catalysts", [])
    if not isinstance(catalysts, list):
        issues.append("catalysts must be a list")
    for idx, catalyst in enumerate(catalysts):
        issues.extend(collect_missing_fields(catalyst, REQUIRED_CATALYST_FIELDS, f"catalysts[{idx}]"))

    if issues:
        raise ValueError("Invalid research pack input:\n- " + "\n- ".join(issues))

    return {
        "valid": True,
        "counts": {
            "stack_layers": len(stack_layers),
            "companies": len(companies),
            "evidence": len(evidence),
            "catalysts": len(catalysts),
        },
    }


def normalize_evidence(records: list[dict]) -> list[dict]:
    out = []
    for index, item in enumerate(records):
        normalized = dict(item)
        if not normalized.get("label"):
            normalized["label"] = TIER_TO_LABEL.get(normalized.get("tier", "").upper(), "Needs verification")
        normalized["strength_rank"] = EVIDENCE_ORDER.get(normalized["label"], 1)
        normalized["_input_index"] = index
        out.append(normalized)
    return sorted(out, key=lambda x: (-x["strength_rank"], x["_input_index"]))


def average_company_scores(companies: list[dict]) -> dict:
    scores = {}
    for dim in SCORE_FIELDS:
        values = [c[dim] for c in companies if dim in c]
        scores[dim] = round(mean(values), 2) if values else 0
    scores["total_average"] = round(mean(scores[d] for d in SCORE_FIELDS), 2) if companies else 0
    return scores


def lane_priority(total_average: float) -> str:
    if total_average >= 4.2:
        return "Very high-priority lane"
    if total_average >= 3.6:
        return "High-priority lane"
    if total_average >= 3.0:
        return "Watch closely"
    return "Lower-priority lane for now"


def build_graph(data: dict, evidence: list[dict]) -> dict:
    nodes = []
    edges = []

    thesis = data["thesis"]
    nodes.append({"id": "end_system", "type": "end_system", "label": thesis["end_system"]})

    for layer in data.get("stack_layers", []):
        layer_id = f"layer_{layer['id']}"
        nodes.append({"id": layer_id, "type": "component", "label": layer["label"]})
        edges.append({"from": "end_system", "to": layer_id, "type": "depends_on"})

    for company in data.get("companies", []):
        cid = f"company_{company['ticker'].lower()}"
        nodes.append({"id": cid, "type": "company", "label": company["name"]})
        layer_id = f"layer_{company['stack_layer']}"
        edges.append({"from": cid, "to": layer_id, "type": "supplies"})

    for record in evidence:
        eid = record["id"]
        nodes.append({"id": eid, "type": "evidence", "label": f"{record['entity']}: {record['title']}"})
        company_match = next(
            (c for c in data.get("companies", []) if c["name"] == record["entity"] or c["ticker"] == record["entity"]),
            None,
        )
        if company_match:
            edges.append({"from": f"company_{company_match['ticker'].lower()}", "to": eid, "type": "confirmed_by"})

    for idx, catalyst in enumerate(data.get("catalysts", []), start=1):
        cat_id = f"catalyst_{idx}"
        nodes.append({"id": cat_id, "type": "catalyst", "label": catalyst["label"]})
        for company in data.get("companies", [])[:3]:
            edges.append({"from": f"company_{company['ticker'].lower()}", "to": cat_id, "type": "catalyzed_by"})

    return {"nodes": nodes, "edges": edges}


def strongest_evidence(evidence: list[dict]) -> dict | None:
    return evidence[0] if evidence else None


def compute_name_average(company: dict) -> float:
    return round(mean([company[field] for field in SCORE_FIELDS]), 2)


def top_names(companies: list[dict], top_n: int = 3) -> list[dict]:
    def rank(company: dict) -> tuple[float, float]:
        return (compute_name_average(company), company["market_cap_usd_b"] * -1)

    return sorted(companies, key=rank, reverse=True)[:top_n]


def stack_summary(data: dict, max_layers: int = 5) -> list[str]:
    layers = data.get("stack_layers", [])[:max_layers]
    return [f"{layer['id']}: {layer['label']}" for layer in layers]


def compact_quote(record: dict) -> str | None:
    snippets = record.get("quote_snippets") or []
    return snippets[0] if snippets else None


def build_evidence_trace(evidence: list[dict], companies: list[dict]) -> list[dict]:
    company_by_name = {company["name"]: company for company in companies}
    company_by_ticker = {company["ticker"]: company for company in companies}
    trace = []
    for record in evidence:
        company = company_by_name.get(record["entity"]) or company_by_ticker.get(record["entity"])
        trace.append(
            {
                "id": record["id"],
                "entity": record["entity"],
                "title": record["title"],
                "label": record["label"],
                "tier": record["tier"],
                "source_type": record.get("source_type"),
                "source_confidence": record.get("source_confidence", "Medium"),
                "summary": record["summary"],
                "quote_snippets": record.get("quote_snippets", []),
                "signals": record.get("signals", []),
                "link_reason": record.get("link_reason", "Directly relevant to the current lane."),
                "linked_company": company["ticker"] if company else None,
                "linked_role": company["role"] if company else None,
                "url": record["url"],
            }
        )
    return trace


def render_evidence_trace(title: str, evidence_trace: list[dict]) -> str:
    lines = [f"# Evidence Trace - {title}", ""]
    for idx, item in enumerate(evidence_trace, start=1):
        lines.extend(
            [
                f"## {idx}. {item['entity']} - {item['title']}",
                f"- Label: {item['label']}",
                f"- Confidence: {item['source_confidence']}",
                f"- Source type: {item.get('source_type', 'unknown')}",
                f"- Link reason: {item['link_reason']}",
            ]
        )
        if item.get("linked_company"):
            lines.append(f"- Linked company: {item['linked_company']} ({item.get('linked_role', 'n/a')})")
        if item.get("signals"):
            lines.append(f"- Signals: {', '.join(item['signals'])}")
        lines.extend(["", "### Summary", item["summary"]])
        snippets = item.get("quote_snippets", [])
        if snippets:
            lines.extend(["", "### Quote Snippets"])
            for snippet in snippets:
                lines.append(f"> {snippet}")
        lines.extend(["", f"Source: {item['url']}", ""])
    return "\n".join(lines).rstrip() + "\n"


def render_quick_scan(data: dict, evidence: list[dict], lane_scores: dict) -> str:
    thesis = data["thesis"]
    strongest = strongest_evidence(evidence)
    bottlenecks = data.get("bottlenecks", [])
    lines = [
        f"# Quick Scan - {data['meta']['title']}",
        "",
        "## Thesis",
        thesis["thesis_sentence"],
        "",
        "## End System",
        f"- {thesis['end_system']}",
        "",
        "## Stack Summary",
    ]
    for line in stack_summary(data):
        lines.append(f"- {line}")
    lines.extend(["", "## Primary Bottleneck", f"- {thesis['bottleneck_call']}"])
    if bottlenecks:
        lines.extend(["", "## Bottleneck Detail"])
        for item in bottlenecks:
            lines.append(f"- {item['label']} ({item['type']}): {item['why_it_matters']}")
    if strongest:
        quote = compact_quote(strongest)
        lines.extend(
            [
                "",
                "## Strongest Evidence",
                f"- [{strongest['label']}] {strongest['entity']} - {strongest['summary']}",
                f"- Confidence: {strongest.get('source_confidence', 'Medium')}",
                f"- Source: {strongest['url']}",
            ]
        )
        if quote:
            lines.append(f'- Quote: "{quote}"')
    lines.extend(
        [
            "",
            "## Lane Score",
            f"- Constraint: {lane_scores['constraint_score']}/5",
            f"- Evidence: {lane_scores['evidence_score']}/5",
            f"- Consensus: {lane_scores['consensus_score']}/5",
            f"- Mispricing: {lane_scores['mispricing_score']}/5",
            f"- Catalyst: {lane_scores['catalyst_score']}/5",
            f"- Priority: {lane_priority(lane_scores['total_average'])}",
            "",
            "## Next Checks",
            "- Next earnings commentary on AI mix and lead times",
            "- Packaging / power / cooling capacity updates",
            "- Whether end-demand remains strong enough to sustain capex",
        ]
    )
    return "\n".join(lines) + "\n"


def render_evidence_memo(data: dict, evidence: list[dict], lane_scores: dict, top_companies: list[dict]) -> str:
    thesis = data["thesis"]
    lines = [
        f"# Evidence Memo - {data['meta']['title']}",
        "",
        "## Direction",
        thesis["supertrend"],
        "",
        "## Lane",
        thesis["lane"],
        "",
        "## Stack Summary",
    ]
    for line in stack_summary(data, max_layers=len(data.get("stack_layers", []))):
        lines.append(f"- {line}")
    lines.extend(
        [
            "",
            "## Why This Lane",
            thesis["thesis_sentence"],
            "",
            "## Evidence Ladder",
        ]
    )
    for item in evidence:
        lines.append(
            f"- [{item['label']}] {item['entity']} - {item['summary']} ({item['url']}) | confidence: {item.get('source_confidence', 'Medium')}"
        )
        if item.get("link_reason"):
            lines.append(f"  - link reason: {item['link_reason']}")
        quote = compact_quote(item)
        if quote:
            lines.append(f'  - quote: "{quote}"')
    lines.extend(
        [
            "",
            "## Weakest Assumption",
            f"- {thesis['weakest_assumption']}",
            "",
            "## Thesis Breaker",
            f"- {thesis['thesis_breaker']}",
            "",
            "## Top Names To Watch",
        ]
    )
    for company in top_companies:
        lines.append(
            f"- {company['ticker']} / {company['name']}: {company['role']} | market cap ~ ${company['market_cap_usd_b']}B | risk: {company['risk']}"
        )
    lines.extend(
        [
            "",
            "## Lane Score Summary",
            f"- Total average: {lane_scores['total_average']}/5",
            f"- Priority: {lane_priority(lane_scores['total_average'])}",
        ]
    )
    return "\n".join(lines) + "\n"


def render_graph_card(data: dict, graph: dict) -> str:
    lines = [
        f"# Graph Card - {data['meta']['title']}",
        "",
        "## End System",
        f"- {data['thesis']['end_system']}",
        "",
        "## Critical Components",
    ]
    for item in data.get("bottlenecks", []):
        lines.append(f"- {item['label']}")
    lines.extend(["", "## Key Companies"])
    for company in data.get("companies", [])[:6]:
        lines.append(f"- {company['ticker']} / {company['name']} - {company['role']} ({company['stack_layer']})")
    lines.extend(
        [
            "",
            "## Graph Summary",
            f"- Nodes: {len(graph['nodes'])}",
            f"- Edges: {len(graph['edges'])}",
            "- Mermaid preview saved as `graph_mermaid.md`",
        ]
    )
    return "\n".join(lines) + "\n"


def render_catalyst_watch(data: dict, top_companies: list[dict]) -> str:
    lines = [f"# Catalyst Watch - {data['meta']['title']}", "", "## Next Events"]
    for item in data.get("catalysts", []):
        lines.append(f"- {item['label']}: {item['watch_for']}")
    lines.extend(
        [
            "",
            "## Bullish Confirmation",
            "- Management teams continue to describe AI demand, deployment, or capacity spend as durable rather than transitory.",
            "",
            "## Bearish Confirmation",
            "- Lead times compress abruptly or management signals weaker expansion plans than expected.",
            "",
            "## Most Sensitive Names",
        ]
    )
    for company in top_companies:
        lines.append(f"- {company['ticker']} / {company['name']}")
    return "\n".join(lines) + "\n"


def build_scorecard(data: dict, lane_scores: dict, top_companies: list[dict]) -> dict:
    names = []
    for company in data.get("companies", []):
        name_total = compute_name_average(company)
        names.append(
            {
                "ticker": company["ticker"],
                "name": company["name"],
                "role": company["role"],
                "stack_layer": company["stack_layer"],
                "market_cap_usd_b": company["market_cap_usd_b"],
                "scores": {
                    "constraint": company["constraint_score"],
                    "evidence": company["evidence_score"],
                    "consensus": company["consensus_score"],
                    "mispricing": company["mispricing_score"],
                    "catalyst": company["catalyst_score"],
                    "total_average": name_total,
                },
                "risk": company["risk"],
                "source_confidence": company.get("source_confidence"),
                "evidence_count": company.get("evidence_count"),
            }
        )
    return {
        "lane": {
            "name": data["thesis"]["lane"],
            "scores": lane_scores,
            "priority": lane_priority(lane_scores["total_average"]),
        },
        "top_names": [company["ticker"] for company in top_companies],
        "names": sorted(names, key=lambda x: x["scores"]["total_average"], reverse=True),
    }


def render_mermaid_graph(graph: dict) -> str:
    type_shapes = {
        "end_system": ('(["', '"])'),
        "component": ('["', '"]'),
        "company": ('[["', '"]]'),
        "evidence": ('{{"', '"}}'),
        "catalyst": ('(["', '"])'),
    }
    lines = ["flowchart TD"]
    node_types = {}
    for node in graph["nodes"]:
        left, right = type_shapes.get(node["type"], ('["', '"]'))
        label = str(node["label"]).replace('"', "'")
        lines.append(f'    {node["id"]}{left}{label}{right}')
        node_types[node["id"]] = node["type"]
    for edge in graph["edges"]:
        edge_label = edge["type"].replace("_", " ")
        lines.append(f'    {edge["from"]} -->|{edge_label}| {edge["to"]}')

    lines.extend(
        [
            "",
            "    classDef end_system fill:#0b3b66,stroke:#8fd3ff,color:#ffffff;",
            "    classDef component fill:#132a3d,stroke:#6bb7ff,color:#eef7ff;",
            "    classDef company fill:#0d3d2c,stroke:#72e3b1,color:#f3fffb;",
            "    classDef evidence fill:#4a3213,stroke:#f6c86d,color:#fff7e8;",
            "    classDef catalyst fill:#3d123f,stroke:#df8eff,color:#fff1ff;",
        ]
    )
    for node_id, node_type in node_types.items():
        lines.append(f"    class {node_id} {node_type};")
    return "\n".join(lines) + "\n"


def render_mermaid_markdown(mermaid: str, title: str) -> str:
    return f"# Graph Mermaid - {title}\n\n```mermaid\n{mermaid}```\n"


def build_research_pack(data: dict) -> dict:
    validation = validate_input(data)
    evidence = normalize_evidence(data.get("evidence", []))
    lane_scores = average_company_scores(data.get("companies", []))
    graph = build_graph(data, evidence)
    mermaid = render_mermaid_graph(graph)
    top_companies = top_names(data.get("companies", []))
    scorecard = build_scorecard(data, lane_scores, top_companies)
    evidence_trace = build_evidence_trace(evidence, data.get("companies", []))
    research_pack = {
        "meta": data["meta"],
        "thesis": data["thesis"],
        "lane_score": lane_scores,
        "lane_priority": lane_priority(lane_scores["total_average"]),
        "top_names": top_companies,
        "evidence": evidence,
        "evidence_trace": evidence_trace,
        "graph_summary": {"nodes": len(graph["nodes"]), "edges": len(graph["edges"])},
        "catalysts": data.get("catalysts", []),
    }
    return {
        "validation": validation,
        "evidence": evidence,
        "lane_scores": lane_scores,
        "graph": graph,
        "mermaid": mermaid,
        "top_companies": top_companies,
        "scorecard": scorecard,
        "evidence_trace": evidence_trace,
        "research_pack": research_pack,
    }


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a Chokepoint Atlas research pack from structured JSON input.")
    parser.add_argument("--input", required=True, help="Path to the structured lane input JSON")
    parser.add_argument("--output", required=True, help="Output directory for the generated research pack")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    ensure_dir(output_dir)

    data = load_json(input_path)
    bundle = build_research_pack(data)

    write_json(output_dir / "validation_report.json", bundle["validation"])
    write_json(output_dir / "research_pack.json", bundle["research_pack"])
    write_json(output_dir / "graph.json", bundle["graph"])
    write_json(output_dir / "scorecard.json", bundle["scorecard"])
    write_json(output_dir / "evidence_trace.json", bundle["evidence_trace"])
    write_text(output_dir / "quick_scan.md", render_quick_scan(data, bundle["evidence"], bundle["lane_scores"]))
    write_text(
        output_dir / "evidence_memo.md",
        render_evidence_memo(data, bundle["evidence"], bundle["lane_scores"], bundle["top_companies"]),
    )
    write_text(output_dir / "evidence_trace.md", render_evidence_trace(data["meta"]["title"], bundle["evidence_trace"]))
    write_text(output_dir / "graph_card.md", render_graph_card(data, bundle["graph"]))
    write_text(output_dir / "catalyst_watch.md", render_catalyst_watch(data, bundle["top_companies"]))
    write_text(output_dir / "graph.mmd", bundle["mermaid"])
    write_text(output_dir / "graph_mermaid.md", render_mermaid_markdown(bundle["mermaid"], data["meta"]["title"]))

    print(f"Built research pack at: {output_dir}")


if __name__ == "__main__":
    main()
