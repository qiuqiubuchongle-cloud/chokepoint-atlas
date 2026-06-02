#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from build_research_pack import build_research_pack, render_catalyst_watch, render_evidence_memo, render_graph_card, render_mermaid_markdown, render_quick_scan, write_json, write_text
from extract_sources_to_pack import build_draft_pack, ensure_dir, load_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the full source-bundle -> draft pack -> final research pack pipeline.")
    parser.add_argument("--input", required=True, help="Path to a source bundle JSON")
    parser.add_argument("--output", required=True, help="Output directory for the full pipeline artifacts")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    ensure_dir(output_dir)

    payload = load_json(input_path)
    draft_pack, extraction_report = build_draft_pack(payload)
    bundle = build_research_pack(draft_pack)

    draft_dir = output_dir / "01_draft"
    final_dir = output_dir / "02_final_pack"
    ensure_dir(draft_dir)
    ensure_dir(final_dir)

    write_json(draft_dir / "draft_pack_input.json", draft_pack)
    write_json(draft_dir / "extraction_report.json", extraction_report)

    write_json(final_dir / "validation_report.json", bundle["validation"])
    write_json(final_dir / "research_pack.json", bundle["research_pack"])
    write_json(final_dir / "graph.json", bundle["graph"])
    write_json(final_dir / "scorecard.json", bundle["scorecard"])
    write_text(final_dir / "quick_scan.md", render_quick_scan(draft_pack, bundle["evidence"], bundle["lane_scores"]))
    write_text(
        final_dir / "evidence_memo.md",
        render_evidence_memo(draft_pack, bundle["evidence"], bundle["lane_scores"], bundle["top_companies"]),
    )
    write_text(final_dir / "graph_card.md", render_graph_card(draft_pack, bundle["graph"]))
    write_text(final_dir / "catalyst_watch.md", render_catalyst_watch(draft_pack, bundle["top_companies"]))
    write_text(final_dir / "graph.mmd", bundle["mermaid"])
    write_text(final_dir / "graph_mermaid.md", render_mermaid_markdown(bundle["mermaid"], draft_pack["meta"]["title"]))

    print(f"Built full source pipeline at: {output_dir}")


if __name__ == "__main__":
    main()
