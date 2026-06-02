# Chokepoint Atlas

`Chokepoint Atlas` is a reusable research skill for finding real bottlenecks in AI infrastructure supply chains.

## 中文

**Chokepoint Atlas** 是一个面向 AI 基础设施研究的 Agent Skill。

它不是上来就给股票代码的选股 prompt。  
它更像一个研究助手，专门帮你做一件事：

**把热门 AI 叙事拆成真实供应链，再找出最容易卡脖子的那一层。**

核心流程很简单：

1. 先确认终端系统
2. 再拆供应链栈
3. 找真正的瓶颈
4. 用财报、研报、产业新闻交叉验证
5. 先给方向，再给名字

它适合拿来研究：

- AI 光通信
- 封装与测试
- 数据中心供电
- 液冷与热管理
- 机器人供应链
- 其他 AI 基础设施方向

它不适合：

- 直接要短线代码
- 只想看情绪和热度
- 不想看逻辑、只想抄答案

一句话说：

**Chokepoint Atlas 不是帮你追热点，而是帮你先找到真正会堵车的地方。**

## English

**Chokepoint Atlas** is an agent skill for AI infrastructure research.

It is not a stock-picking prompt that jumps straight to tickers.  
It is a research workflow designed to do one thing well:

**turn broad AI narratives into real supply-chain maps, then identify the layer most likely to become a bottleneck.**

The workflow is straightforward:

1. Define the end system
2. Map the supply-chain stack
3. Find the real constraint
4. Cross-check with earnings, reports, and industry news
5. Output the direction first, then candidate names

It is useful for researching:

- AI optical interconnect
- packaging and testing
- datacenter power delivery
- liquid cooling and thermal management
- humanoid robotics supply chains
- other AI infrastructure lanes

It is not meant for:

- instant ticker dumping
- momentum-only workflows
- users who want answers without thesis building

In one line:

**Chokepoint Atlas does not help you chase noise. It helps you find where the system will actually break first.**

## Install

Install the skill as `ai-supply-chain-bottleneck-hunter`:

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

## Repository Contents

- [SKILL.md](./SKILL.md): the main skill
- [中文产品说明](./docs/PRODUCT_CN.md)
- [English product description](./docs/PRODUCT_EN.md)
- [2.0 产品规划](./docs/PRODUCT_PLAN_V2_CN.md)
- [Product manual](./references/product-manual.md)
- [Infographic copy](./docs/INFOGRAPHIC_COPY.md)

## Local MVP

This repo now includes a small local MVP that turns structured lane input into a reusable research pack.

Run:

```bash
python3 scripts/build_research_pack.py \
  --input examples/ai_factory_lane_input.json \
  --output out/ai_factory_demo
```

Generated outputs include:

- `research_pack.json`
- `quick_scan.md`
- `evidence_memo.md`
- `graph.json`
- `graph.mmd`
- `graph_mermaid.md`
- `graph_card.md`
- `scorecard.json`
- `validation_report.json`
- `catalyst_watch.md`

## Lane Comparison

You can also compare multiple lanes in one run:

```bash
python3 scripts/compare_lanes.py \
  --input examples/lane_compare_input.json \
  --output out/lane_compare_demo
```

Generated outputs include:

- `lane_ranking.json`
- `lane_details.json`
- `ranked_lane_table.md`
- `lane_compare_memo.md`

## Source Pipeline

You can also start from a looser source bundle and let the repo build the draft input plus the final pack:

```bash
python3 scripts/run_source_pipeline.py \
  --input examples/source_bundle_input.json \
  --output out/source_pipeline_demo
```

This pipeline produces:

- `01_draft/draft_pack_input.json`
- `01_draft/extraction_report.json`
- `02_final_pack/research_pack.json`
- `02_final_pack/quick_scan.md`
- `02_final_pack/evidence_memo.md`
- `02_final_pack/graph.json`
- `02_final_pack/graph.mmd`
- `02_final_pack/graph_mermaid.md`
- `02_final_pack/scorecard.json`
- `02_final_pack/validation_report.json`

## Product Snapshot

![AI Bottleneck Hunter infographic](./assets/ai-bottleneck-hunter-infographic.png)
