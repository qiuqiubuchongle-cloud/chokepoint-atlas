# Chokepoint Atlas Product Description

## What the product does

Chokepoint Atlas is a research product for AI infrastructure bottleneck analysis.

It does not begin by dumping stock tickers.

It begins by turning a broad AI theme into:

- a real system
- a supply-chain stack
- a bottleneck thesis
- an evidence trail
- a reusable research pack

In one line:

**It turns AI narrative into supply-chain research.**

---

## The current product logic

The product logic is simple. It runs in four steps.

### 1. Start from a real system

The workflow does not start with vague ideas like “AI is growing” or “compute demand is exploding.”

It starts with a real system, for example:

- NVIDIA DSX AI Factory
- a TPU pod
- an advanced-packaging lane
- datacenter power and liquid cooling

First define the machine. Then define the chain around it.

### 2. Map the stack

Once the system is chosen, the product breaks it into layers:

- end demand
- system integration
- components
- test and packaging
- upstream materials and tooling

The goal is to turn noisy market conversation into a researchable industrial structure.

### 3. Find the choke point, then pull evidence

The key question is not “which stock goes up.”

The key question is:

**If demand keeps scaling, which layer breaks first?**

Then the product pulls and structures evidence from:

- earnings
- calls and transcripts
- official product pages
- industry articles
- sell-side or IR-style summaries

And it does not stop at summary. It now keeps:

- evidence labels
- extracted signals
- quote snippets
- source confidence
- link reasons

That means it can explain not only *what the thesis is*, but also *which line of evidence supports it*.

### 4. Output a reusable research pack

Instead of producing one block of analysis, the product generates a bundle of artifacts such as:

- `quick_scan.md`
- `evidence_memo.md`
- `evidence_trace.md`
- `graph.json`
- `graph_mermaid.md`
- `scorecard.json`
- `catalyst_watch.md`

So the product is best understood as:

**theme input -> structured research -> reusable output artifacts**

---

## Current usage modes

The product currently has three main entry points.

### Mode 1: Single-lane research pack

Use this when:

- you already know the lane you want to study
- you want one standardized research pack

Script:

`scripts/build_research_pack.py`

Example input:

`examples/ai_factory_lane_input.json`

Outputs include:

- `research_pack.json`
- `quick_scan.md`
- `evidence_memo.md`
- `evidence_trace.json`
- `evidence_trace.md`
- `graph.json`
- `graph.mmd`
- `graph_mermaid.md`
- `graph_card.md`
- `scorecard.json`
- `validation_report.json`
- `catalyst_watch.md`

---

### Mode 2: Multi-lane comparison

Use this when:

- you want to compare several lanes
- you want ranking and priority instead of one isolated thesis

Script:

`scripts/compare_lanes.py`

Example input:

`examples/lane_compare_input.json`

Outputs include:

- `lane_ranking.json`
- `lane_details.json`
- `ranked_lane_table.md`
- `lane_compare_memo.md`

This is the step where the product moves from studying one thesis to comparing multiple theses.

---

### Mode 3: Source-bundle pipeline

Use this when:

- you already have raw materials
- you do not want to hand-build the final pack JSON
- you want the product to turn loose inputs into a final research pack

Script:

`scripts/run_source_pipeline.py`

Example input:

`examples/source_bundle_input.json`

The pipeline outputs two layers.

#### Layer 1: Draft input

Directory:

`01_draft/`

Artifacts:

- `draft_pack_input.json`
- `extraction_report.json`

This layer:

- extracts structured evidence from the source bundle
- extracts signals
- extracts quote snippets
- assigns source confidence
- writes link reasons
- fills initial company scoring fields

#### Layer 2: Final research pack

Directory:

`02_final_pack/`

Artifacts:

- `research_pack.json`
- `quick_scan.md`
- `evidence_memo.md`
- `evidence_trace.json`
- `evidence_trace.md`
- `graph.json`
- `graph.mmd`
- `graph_mermaid.md`
- `graph_card.md`
- `scorecard.json`
- `validation_report.json`
- `catalyst_watch.md`

This is where the product starts to feel less like a prompt and more like a research pipeline.

---

## How this differs from “ask AI what to buy”

A generic workflow usually looks like this:

- ask AI for names
- ask AI to summarize a report
- ask AI whether a sector has upside

This product uses a stricter order:

1. define the system
2. map the stack
3. identify the bottleneck
4. gather and rank evidence
5. then produce direction, names, and priority

That difference matters.

**The product is not trying to let AI guess for you. It is trying to make the research process more rigorous.**

---

## Where the product is strongest right now

The current version is strongest in four areas.

### 1. Standardized structure

Whether the input is one lane or several, the outputs are now much more consistent.

### 2. Evidence is no longer just summary

The product now preserves:

- quote snippets
- source confidence
- link reasons

So it is starting to build an actual evidence trail.

### 3. Graph outputs are real artifacts

The product does not stop at prose. It generates:

- `graph.json`
- `graph.mmd`
- `graph_mermaid.md`

That makes future visualization much easier.

### 4. Priority can be compared

The system no longer analyzes only one idea at a time. It can compare which lane deserves the next research block.

---

## Who this is for

Good fit:

- AI infrastructure researchers
- analysts who want to systematize supply-chain work
- agents that need a structured research protocol
- users who want to turn messy inputs into reusable outputs

Poor fit:

- users who only want fast ticker ideas
- users focused only on hype and sentiment
- users looking for AI to replace judgment with instant answers

---

## What is still unfinished

This already feels like a product, but it is not finished.

The next two meaningful upgrades would be:

### 1. Finer-grained evidence extraction

Examples:

- publish time
- source domain
- claim type
- quote offsets

### 2. Evidence-linked graph interaction

In other words:

click a graph node, jump to the exact supporting quote and source.

Once those are added, the product becomes much stronger as a research system.

---

## Bottom line

Chokepoint Atlas is no longer just a prompt for “give me a few names.”

It is becoming:

**a product that turns AI narratives into supply-chain structure, evidence trails, and reusable research deliverables.**
