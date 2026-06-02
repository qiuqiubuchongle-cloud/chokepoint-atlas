#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_research_pack import build_research_pack, ensure_dir, lane_priority, load_json, write_json, write_text


def render_ranked_lane_table(rows: list[dict]) -> str:
    lines = [
        "# Ranked Lane Table",
        "",
        "| Rank | Lane | End System | Constraint | Evidence | Consensus | Mispricing | Catalyst | Total | Priority |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for idx, row in enumerate(rows, start=1):
        score = row["lane_score"]
        lines.append(
            "| {rank} | {lane} | {end_system} | {constraint} | {evidence} | {consensus} | {mispricing} | {catalyst} | {total} | {priority} |".format(
                rank=idx,
                lane=row["lane"],
                end_system=row["end_system"],
                constraint=score["constraint_score"],
                evidence=score["evidence_score"],
                consensus=score["consensus_score"],
                mispricing=score["mispricing_score"],
                catalyst=score["catalyst_score"],
                total=score["total_average"],
                priority=row["priority"],
            )
        )
    return "\n".join(lines) + "\n"


def render_lane_compare_memo(rows: list[dict]) -> str:
    lines = [
        "# Lane Compare Memo",
        "",
        "## Ranking Logic",
        "- Compare lanes on constraint, evidence, consensus gap, mispricing, and catalyst timing.",
        "- Goal is not to fake precision. Goal is to decide what deserves the next block of research time.",
        "",
        "## Ranked Summary",
    ]
    for idx, row in enumerate(rows, start=1):
        lines.extend(
            [
                f"### {idx}. {row['lane']}",
                f"- End system: {row['end_system']}",
                f"- Priority: {row['priority']}",
                f"- Total score: {row['lane_score']['total_average']}/5",
                f"- Bottleneck: {row['bottleneck_call']}",
                f"- Strongest evidence: {row['strongest_evidence']}",
                f"- Top names: {', '.join(row['top_names'])}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare multiple Chokepoint Atlas lanes from a single input file.")
    parser.add_argument("--input", required=True, help="Path to a JSON file with a top-level `lanes` array")
    parser.add_argument("--output", required=True, help="Output directory for the lane-comparison artifacts")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    ensure_dir(output_dir)

    payload = load_json(input_path)
    if "lanes" not in payload or not isinstance(payload["lanes"], list) or not payload["lanes"]:
        raise ValueError("Input must contain a non-empty top-level `lanes` array.")

    rows = []
    detailed = []
    for lane in payload["lanes"]:
        bundle = build_research_pack(lane)
        strongest = bundle["evidence"][0]["summary"] if bundle["evidence"] else "No evidence"
        row = {
            "pack_id": lane["meta"]["pack_id"],
            "title": lane["meta"]["title"],
            "lane": lane["thesis"]["lane"],
            "end_system": lane["thesis"]["end_system"],
            "bottleneck_call": lane["thesis"]["bottleneck_call"],
            "lane_score": bundle["lane_scores"],
            "priority": lane_priority(bundle["lane_scores"]["total_average"]),
            "strongest_evidence": strongest,
            "top_names": [name["ticker"] for name in bundle["top_companies"]],
        }
        rows.append(row)
        detailed.append(
            {
                "pack_id": lane["meta"]["pack_id"],
                "bundle": bundle["research_pack"],
                "top_names": bundle["top_companies"],
            }
        )

    rows.sort(key=lambda x: x["lane_score"]["total_average"], reverse=True)

    write_json(output_dir / "lane_ranking.json", {"lanes": rows})
    write_json(output_dir / "lane_details.json", {"lanes": detailed})
    write_text(output_dir / "ranked_lane_table.md", render_ranked_lane_table(rows))
    write_text(output_dir / "lane_compare_memo.md", render_lane_compare_memo(rows))

    print(f"Built lane comparison pack at: {output_dir}")


if __name__ == "__main__":
    main()
