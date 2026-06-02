# Choke Atlas

`Choke Atlas` is a Codex skill for AI infrastructure research.

It helps an agent move from a broad AI or crypto theme to a concrete bottleneck, market structure thesis, candidate asset list, and current market setup.

The short version:

> Map the stack. Grade the evidence. Pick candidates carefully. Check the current tape before talking entry and exit zones.

## What It Does

Choke Atlas is designed for research around AI infrastructure lanes such as:

- optical interconnect and photonics
- advanced packaging and test
- datacenter power delivery
- liquid cooling and thermal management
- semiconductor materials and substrates
- robotics and other physical AI supply chains
- crypto majors, AI tokens, DePIN tokens, miners, and crypto infrastructure

The skill can:

- break a theme into a 6-9 layer supply-chain stack
- identify the layer most likely to become a real bottleneck
- grade the thesis with an evidence scorecard
- let the agent select candidate stocks or crypto assets when the user does not provide tickers
- check current market data before producing timing-related output
- build scenario-based entry, add, invalidation, and target zones
- apply crypto-specific checks such as BTC/ETH regime, funding, open interest, tokenomics, unlocks, and liquidity

## What It Is Not

This is not a magic stock picker, auto-trader, or guaranteed signal engine.

It should not jump straight to tickers. It should first explain why a layer matters, what evidence supports it, what could break the thesis, and whether the current price setup is actually clean.

Entry and exit levels are treated as research scenarios, not personalized financial advice.

## Example Prompts

Direction first:

```text
Use $choke-atlas to find the next AI infrastructure bottleneck. Do not give me stocks yet.
```

Agent-selected candidates:

```text
Use $choke-atlas. Pick the best AI infrastructure candidates yourself, then give live setups.
```

Single-name workup:

```text
Use $choke-atlas to underwrite AXTI and explain where it sits in the AI infrastructure stack.
```

Live market setup:

```text
Use $choke-atlas to screen AI optical interconnect names today. Rank them by thesis grade, setup grade, liquidity, catalyst timing, and risk/reward clarity.
```

Crypto setup:

```text
Use $choke-atlas to analyze crypto today. Pick AI/DePIN tokens yourself, check BTC/ETH regime, funding, unlocks, liquidity, and give scenario-based entry/exit zones.
```

## Install

Install the skill as `choke-atlas`:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo qiuqiubuchongle-cloud/chokepoint-atlas \
  --path . \
  --name choke-atlas
```

If the default download mode fails, use git mode:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo qiuqiubuchongle-cloud/chokepoint-atlas \
  --path . \
  --name choke-atlas \
  --method git
```

Restart Codex after installation so the skill is picked up.

## Files

- [SKILL.md](./SKILL.md): main skill instructions
- [references/evidence-scorecard.md](./references/evidence-scorecard.md): evidence grading and bottleneck scoring
- [references/live-market-playbook.md](./references/live-market-playbook.md): current market setup workflow
- [references/crypto-market-playbook.md](./references/crypto-market-playbook.md): crypto market structure and token setup workflow
- [references/output-formats.md](./references/output-formats.md): response templates
- [references/product-manual.md](./references/product-manual.md): fuller usage guide
- [docs/PRODUCT_CN.md](./docs/PRODUCT_CN.md): Chinese product notes
- [docs/PRODUCT_EN.md](./docs/PRODUCT_EN.md): English product notes

## Product Snapshot

![Choke Atlas infographic](./assets/ai-bottleneck-hunter-infographic.png)
