# Chokepoint Atlas

`Chokepoint Atlas` is a reusable research skill for AI supply-chain analysis.

说人话一点：

它不是让 agent 上来就给你一堆股票代码。

它是让 agent 先回答一个更重要的问题：

**如果 AI 继续扩张，最先卡住的会是哪一环？**

然后再顺着这条线，去找值得继续研究的公司。

## What This Skill Is For

Use it when you want an agent to:

- break a big AI story into a real supply chain
- find the narrowest bottleneck in that chain
- check whether that bottleneck is real or just market narrative
- tell you which layer matters first
- give company names only after the thesis is clear

Typical questions:

- What is the next AI infrastructure bottleneck?
- Is optical / packaging / power / cooling the more important lane now?
- Which companies sit closest to the constraint?
- Which names are real executors, and which are just optionality bets?

## What It Does

The workflow is fixed:

1. Start from a real demand wave
2. Draw the stack
3. Find the bottleneck
4. Verify it with earnings, reports, and industry news
5. Give the direction first
6. Give company names only if you ask for them

This order is the whole point of the product.

## What You Get Back

The skill usually answers in 3 layers:

1. **Direction first**  
   Which part of the supply chain matters most right now, and why.

2. **Watchlist second**  
   Grouped names such as proven executors, pure bottlenecks, second-order beneficiaries, and early optionality.

3. **Single-name deep dive**  
   If you want to drill into one company, it can break down what that company actually does and what could break the thesis.

## Quick Install

If your agent supports GitHub skill install, use:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo qiuqiubuchongle-cloud/chokepoint-atlas \
  --path . \
  --name ai-supply-chain-bottleneck-hunter
```

If the default download mode fails, use git mode:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo qiuqiubuchongle-cloud/chokepoint-atlas \
  --path . \
  --name ai-supply-chain-bottleneck-hunter \
  --method git
```

Then restart Codex so the new skill is picked up.

## How To Ask It

Example 1: direction only

```text
Use $ai-supply-chain-bottleneck-hunter.
Tell me the next AI infrastructure bottleneck.
Start with direction only. Do not give me names yet.
```

Example 2: names after thesis

```text
Continue with $ai-supply-chain-bottleneck-hunter.
Now give me names, grouped into:
- proven executors
- pure bottlenecks
- second-order beneficiaries
- early optionality
```

Example 3: one company

```text
Use $ai-supply-chain-bottleneck-hunter to analyze AXTI.
Tell me where it sits in the stack, why it matters, and what would break the thesis.
```

## Who This Is For

Good fit:

- AI infrastructure researchers
- people building repeatable agent workflows
- anyone who wants thesis first and tickers second

Bad fit:

- users who only want instant stock picks
- momentum-only workflows
- "just tell me what to buy" prompts

## Key Files

- [SKILL.md](./SKILL.md): the skill itself
- [Chinese Product Description](./docs/PRODUCT_CN.md)
- [English Product Description](./docs/PRODUCT_EN.md)
- [Product Manual](./references/product-manual.md)
- [Infographic Copy](./docs/INFOGRAPHIC_COPY.md)

## Product Snapshot

![AI Bottleneck Hunter infographic](./assets/ai-bottleneck-hunter-infographic.png)

## License

No explicit open-source license is included yet. Add one if you want reuse terms to be formalized.
