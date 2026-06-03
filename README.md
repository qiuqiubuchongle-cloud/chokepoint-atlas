# Chokepoint Atlas / AI 供应链卡脖子图谱

🌐 Language / 语言： [中文](./README.md) | [English](./docs/PRODUCT_EN.md)

📘 产品介绍： [中文介绍](./README.md) | [English Intro](./docs/PRODUCT_EN.md)

> 一个把 AI 叙事拆成供应链研究的研究型产品。  
> 先找真实系统，再拆上下游，再找卡点，最后输出证据链、关系图和候选公司研究包。

![Chokepoint Atlas Flowchart](./assets/ai-bottleneck-hunter-infographic.png)

## 这是什么

Chokepoint Atlas 不是一个上来就给你报股票代码的工具。

它更像一条研究流水线：

1. 先选一个真实系统  
   比如 `NVIDIA DSX AI Factory`、`TPU pod`、`先进封装链条`、`数据中心供电和液冷`
2. 再把它拆成供应链栈  
   从需求、系统集成、核心部件、测试封装，一直拆到材料和上游工具
3. 再问一句真正重要的话  
   **如果需求继续放大，哪一层会先堵车？**
4. 最后把证据和关系整理出来  
   形成一套能复用的研究包，而不是一段一次性的 AI 回答

一句话说：

**它是一个把“AI 叙事”翻译成“供应链研究”的产品。**

## 它现在怎么用

目前有 3 条主要入口：

### 1. 单条 thesis 研究包

适合已经知道自己要研究哪条线，想直接生成标准化研究包。

- 脚本：`scripts/build_research_pack.py`
- 示例输入：`examples/ai_factory_lane_input.json`

典型输出：

- `quick_scan.md`
- `evidence_memo.md`
- `evidence_trace.md`
- `graph.json`
- `graph_mermaid.md`
- `scorecard.json`
- `catalyst_watch.md`

### 2. 多条 lane 横向比较

适合不只研究一条线，而是想比较哪条更值得深挖。

- 脚本：`scripts/compare_lanes.py`
- 示例输入：`examples/lane_compare_input.json`

典型输出：

- `lane_ranking.json`
- `lane_details.json`
- `ranked_lane_table.md`
- `lane_compare_memo.md`

### 3. 原始材料直出研究包

适合手里已经有新闻、财报、研报、官网材料，不想手工先整理。

- 脚本：`scripts/run_source_pipeline.py`
- 示例输入：`examples/source_bundle_input.json`

这条链路会先抽取：

- evidence
- signal
- quote snippet
- source confidence
- link reason

然后再继续生成最终研究包。

## 它和普通“问 AI 买什么”有什么区别

普通玩法是：

- 问 AI 哪只票好
- 问 AI 帮我总结财报
- 问 AI 这个赛道有没有机会

这个产品的顺序不一样：

- 先定系统
- 再画栈
- 再找瓶颈
- 再拉证据
- 最后才给方向、候选公司和优先级

也就是说：

**它不是让 AI 替你拍脑袋，而是让 AI 帮你把研究流程做扎实。**

## 核心交付物

每条研究线最后不是吐一段话，而是尽量落成一组结构化文件：

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

## 快速入口

- [完整中文产品说明](./docs/PRODUCT_CN.md)
- [English Product Description](./docs/PRODUCT_EN.md)
- [SKILL.md](./SKILL.md)
- [2.0 产品规划](./docs/PRODUCT_PLAN_V2_CN.md)
- [Product Manual](./references/product-manual.md)
