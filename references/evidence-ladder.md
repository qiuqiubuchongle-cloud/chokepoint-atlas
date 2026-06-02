# Evidence Ladder

Use this file when the user wants stronger source discipline, evidence tagging, or a 2.0-style answer.

## Goal

Turn raw materials into ranked evidence instead of treating every source equally.

## Evidence Tiers

### Tier A: Hard Evidence

Use as the strongest support.

- 10-K / 10-Q / annual reports / quarterly reports
- earnings-call transcripts
- investor presentations
- official supplier / customer / partner disclosures
- official product documentation

Default label:

- `Confirmed`

### Tier B: Semi-Hard Evidence

Useful, but not final on its own.

- reputable industry media
- conference or fireside-chat summaries
- sell-side research summaries
- product manuals, procurement docs, tender docs

Default label:

- `Inferred` unless directly quoted from a primary source

### Tier C: Weak Evidence

Helpful as a lead, not as a conclusion.

- X / Twitter posts
- Reddit / forums
- KOL notes
- second-hand screenshots

Default label:

- `Weak`

### Tier D: Unverified Claims

Treat as open leads only.

- rumors
- reposted claims with no original source
- unattributed screenshots

Default label:

- `Needs verification`

## Required Tagging

For every important claim, say one of:

- `Confirmed`
- `Inferred`
- `Weak`
- `Needs verification`

## Good Usage Pattern

For each thesis:

1. strongest proof
2. cross-company confirmation
3. weakest assumption
4. what evidence would upgrade or kill the thesis

## Example

```text
Confirmed:
- Company A said qualification completes in 2H26 in its earnings call.

Inferred:
- If Company B and Company C both describe lead-time pressure in the same layer, the bottleneck is likely real.

Weak:
- Several X accounts are pointing to the same supplier, but no primary disclosure exists yet.

Needs verification:
- A screenshot claims the part is sole-sourced, but no filing or transcript supports it yet.
```
