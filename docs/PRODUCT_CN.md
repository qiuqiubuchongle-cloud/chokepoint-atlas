# Chokepoint Atlas - 产品说明

## 一句话先讲明白

这是一个给 Agent 用的投研 skill。

它不负责上来就给你股票代码。

它负责先把一个大主题拆开，找出真正卡脖子的地方，再告诉你哪些公司值得继续看。

你可以把它理解成：

**一个专门研究 AI 供应链瓶颈的分析助手。**

## 它到底是干嘛的

很多人聊 AI，只会聊最热的那几个名字。

但真正有研究价值的问题，通常是这个：

**如果 AI 继续扩张，最先不够用的会是哪一环？**

比如可能卡在：

- 光模块
- 激光器
- 衬底材料
- 封装
- 电力
- 散热

这个 skill 做的事，就是帮你把这些环节一层层拆出来，然后判断：

1. 哪一层最重要
2. 哪一层最容易卡住
3. 这个卡点是真的，还是市场自己讲出来的故事
4. 真正离这个卡点最近的公司是谁

## 它不是干嘛的

它不是：

- 直接报明牌的选股器
- 短线喊单工具
- 问一句“买什么”就出答案的 magic prompt

如果你只想让它上来吐股票代码，那这个 skill 不适合。

它是先讲逻辑，再给名单。

## 它怎么工作

它的流程固定是这样的：

### 第一步：先定主题

先确定你研究的是哪条线。

比如：

- AI 光通信
- AI 数据中心供电
- 先进封装
- 液冷和热管理
- 人形机器人供应链

### 第二步：拆供应链

把这个主题拆成一层层环节。

不是停留在“这个赛道很火”，而是往下拆：

- 最终需求是什么
- 中间系统是什么
- 核心零件是什么
- 上游材料是什么

### 第三步：找卡点

然后问一个最关键的问题：

**如果需求突然翻倍，最先扛不住的是谁？**

这个“扛不住”可能是：

- 产能跟不上
- 认证周期太长
- 替代品太少
- 良率太低
- 电和热已经到极限

### 第四步：查证据

不是看一条推文就下结论。

它会优先找这些东西：

- 财报
- 电话会
- 官方披露
- 行业新闻
- 供应商和客户的公开信息

最后把结论分清楚：

- 哪些是已经确认的
- 哪些是根据信息推出来的
- 哪些还只是猜测

### 第五步：先给方向，再给名字

默认情况下，它先告诉你：

- 现阶段最值得看的方向是什么
- 为什么是这个方向
- 风险点在哪

如果你继续追问，它才会给你公司名单。

## 现在这个产品已经能跑什么

除了对话式 skill，现在仓库里已经补了一个 **本地可跑的 MVP**。

你可以把它理解成：

**先把研究结果整理成标准输入，再一键生成整套研究包。**

目前能直接产出的文件包括：

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

这意味着它已经不只是“会回答问题”。

它开始具备一点真正产品的味道了：

- 有输入格式
- 有统一输出
- 有研究包沉淀
- 有图谱和评分底稿

## 本地怎么跑

仓库里已经带了一个 demo 输入：

`examples/ai_factory_lane_input.json`

直接运行：

```bash
python3 scripts/build_research_pack.py \
  --input examples/ai_factory_lane_input.json \
  --output out/ai_factory_demo
```

跑完之后，你会在输出目录看到整套研究包：

`out/ai_factory_demo/`

这个 demo 目前演示的是：

- 终端系统：`NVIDIA DSX AI Factory`
- 研究方向：`HBM 测试 + 先进封装支撑工具`
- 输出内容：证据分层、关系图、优先级、催化剂

另外现在还多了两个比较实用的小升级：

- 自动做输入校验，生成 `validation_report.json`
- 自动把 `graph.json` 转成 Mermaid，可直接继续做图

## 现在还支持多条 lane 横向比较

如果你不是只研究一条线，而是想比较：

- 哪条线更值得深挖
- 哪条线证据更硬
- 哪条线只是热闹，哪条线更像真瓶颈

现在可以直接用多 lane compare 入口。

仓库里已经带了一个比较输入：

`examples/lane_compare_input.json`

运行方式：

```bash
python3 scripts/compare_lanes.py \
  --input examples/lane_compare_input.json \
  --output out/lane_compare_demo
```

它会生成：

- `lane_ranking.json`
- `lane_details.json`
- `ranked_lane_table.md`
- `lane_compare_memo.md`

这一步的意义很大，因为它开始把“研究一条 thesis”升级成“比较多个 thesis”。

## 现在还支持 source bundle 一键流水线

如果你已经有一批原始材料，比如：

- 财报摘要
- 官方产品页
- 新闻段落
- IR 文本

你现在不一定要先手动把它们全改成最终 pack JSON。

仓库里已经补了一个更顺手的入口：

`examples/source_bundle_input.json`

先把这些原始材料整理成一个 source bundle，然后直接运行：

```bash
python3 scripts/run_source_pipeline.py \
  --input examples/source_bundle_input.json \
  --output out/source_pipeline_demo
```

它会自动帮你分两步输出：

### 第一步：草稿输入

目录：

`out/source_pipeline_demo/01_draft/`

产物：

- `draft_pack_input.json`
- `extraction_report.json`

这一层做的事是：

- 把 source bundle 里的材料转成结构化 evidence
- 自动抽一些基础 signal
- 给公司补一版初始评分字段

### 第二步：最终研究包

目录：

`out/source_pipeline_demo/02_final_pack/`

产物：

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

这条链路的意义特别直接：

**你不用再手动接两次脚本了。**

它已经开始像一个真正的研究流水线，而不是几段分散工具。

## 这个 MVP 适合拿来干嘛

最适合三件事：

### 1. 做研究底稿

先把一个赛道的核心关系整理进 JSON，再让脚本吐出统一结构。

### 2. 给别的 Agent 接手

很多时候问题不是不会研究，而是每个 Agent 产出的格式都不一样。

现在有了统一的 pack 结构，后续不管是写长推、做信息图，还是继续深挖单票，都会顺很多。

### 3. 做后续产品迭代

后面如果要加：

- 新闻抽取
- 财报抽取
- 图谱可视化
- lane 对 lane 比较

都可以直接接在这个 MVP 上面，不用重新推翻。

## 你会得到什么结果

正常情况下，它会分 3 层输出。

### 1. 方向判断

先告诉你：

- 现在该重点看哪条线
- 真正的瓶颈在哪
- 为什么这个判断成立
- 什么情况会让这个判断失效

### 2. 候选名单

如果你要名字，它不会乱给一堆。

它会分组给你，比如：

- 成熟执行者
- 真正卡脖子的公司
- 二阶受益者
- 早期高波动选手

这样你一眼就知道，哪些更稳，哪些更像赔率票。

### 3. 单家公司深挖

如果你只想看一家公司，它也可以单独拆：

- 这家公司到底卖什么
- 它在整条链里站哪一层
- 为什么它难替代
- 现在证据强不强
- 哪些地方最容易打脸

## 这个 skill 适合谁

适合：

- 想认真研究 AI 基础设施的人
- 想把投研流程交给 Agent 的人
- 不想只听热门故事，想看真实供应链的人

不太适合：

- 只想要短线代码的人
- 只看情绪不看基本面的玩法
- 不愿意先看逻辑、只想直接要答案的人

## 怎么安装

如果你要让别的 Agent 直接安装这个 skill，用这个命令：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo qiuqiubuchongle-cloud/chokepoint-atlas \
  --path . \
  --name ai-supply-chain-bottleneck-hunter
```

如果默认下载方式报错，再用这个：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo qiuqiubuchongle-cloud/chokepoint-atlas \
  --path . \
  --name ai-supply-chain-bottleneck-hunter \
  --method git
```

装完以后，重启 Codex。

## 怎么问，最省事

你可以直接复制这几种问法。

### 问法 1：只要方向，不要名字

```text
Use $ai-supply-chain-bottleneck-hunter.
告诉我下一个 AI 基础设施瓶颈可能在哪。
先只讲方向，不要先给股票代码。
```

### 问法 2：逻辑讲完，再给名单

```text
Continue with $ai-supply-chain-bottleneck-hunter.
现在给我几个公司，分成：
1. 成熟执行者
2. 真瓶颈公司
3. 二阶受益者
4. 早期高波动标的
```

### 问法 3：单独看一家公司

```text
Use $ai-supply-chain-bottleneck-hunter to analyze AXTI.
告诉我它在供应链里处于哪一层，为什么重要，什么情况会打脸。
```

## 为什么它有用

普通人用 AI 做投研，很容易变成一件事：

问 AI 要答案。

这个 skill 更像是在逼 AI 先把问题问对。

因为很多时候，不是你信息太少。

是你一开始问的问题就问偏了。

这个 skill 的价值就在这：

**先把方向问对，再谈公司。**

## 最后一句总结

这不是一个“给我代码”的 prompt。

这是一个把 AI 叙事拆成真实供应链，再把真实供应链拆成可研究方向的 skill。
