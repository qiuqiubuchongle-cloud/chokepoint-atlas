# Chokepoint Atlas / 卡脖子美股战法

## 先一句话说清楚

**这是一个专门用来找“AI 产业链里谁在卡脖子”的美股研究产品。**

如果你想研究 AI、算力、机器人、光通信、先进封装这些方向，但又不想像买 meme 一样瞎冲，这个产品就是帮你先把产业链拆开，看看：

- 到底哪一层最容易堵车
- 哪家公司是真的绕不过去
- 哪些线索只是故事，哪些线索已经有证据

它不是直接喊单的工具。

它做的事情，是把一个热门方向拆开，然后把真正有价值的瓶颈、证据和候选公司整理出来。

一句话说：

**它是一个把“热门叙事”翻译成“供应链研究”的产品。**

---

## 它到底怎么工作

产品逻辑不复杂，核心就是 4 步。

### 1. 先定一个真实系统

不是空谈“AI 会涨”“算力会爆发”。

而是先指定一个真实系统，比如：

- NVIDIA DSX AI Factory
- TPU pod
- 先进封装链条
- 数据中心供电和液冷

先有机器，后有供应链。

### 2. 再拆供应链栈

把这个系统往下拆：

- 最终需求
- 系统集成
- 核心部件
- 测试与封装
- 材料与上游

这一步的目的，是把“大家都在聊的热闹”拆成一张真正能研究的结构图。

### 3. 找卡点，再找证据

它不是先问“哪只票会涨”。

它先问：

**如果需求继续放大，哪一层会先堵车？**

然后再去拉证据：

- 财报
- 电话会
- 官方产品页
- 新闻
- 研报摘要

并且把这些证据结构化，分成：

- evidence label
- signal
- quote snippet
- source confidence
- link reason

也就是不只告诉你“结论是什么”，还告诉你“这句判断是从哪来的”。

### 4. 最后输出研究包

最终不是只吐一段分析，而是产出一整套可复用研究结果，比如：

- `quick_scan.md`
- `evidence_memo.md`
- `evidence_trace.md`
- `graph.json`
- `graph_mermaid.md`
- `scorecard.json`
- `catalyst_watch.md`

你可以把它理解成：

**从主题输入，到结构化研究，再到交付物输出。**

---

## 它适合谁用

适合这几类人：

- 想研究美股 AI 产业链，但不想只看热门大票
- 想找“第二层、第三层瓶颈”这种更有弹性的方向
- 手里已经有一些新闻、财报、研报，想整理成结构化结论
- 想让 Agent 帮你做研究，而不是只让它帮你写摘要

如果你只是想问一句“现在买哪只最猛”，那它不是最适合你的东西。

## 它现在有哪几种用法

现在这个产品已经有 3 条主要入口。

### 用法一：单条 thesis 研究包

适合：

- 已经知道自己要研究哪条线
- 想直接生成一套标准研究包

脚本：

`scripts/build_research_pack.py`

示例输入：

`examples/ai_factory_lane_input.json`

输出包括：

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

### 用法二：多条 lane 横向比较

适合：

- 不只研究一条线
- 想比较哪条线更值得深挖
- 想看优先级排序

脚本：

`scripts/compare_lanes.py`

示例输入：

`examples/lane_compare_input.json`

输出包括：

- `lane_ranking.json`
- `lane_details.json`
- `ranked_lane_table.md`
- `lane_compare_memo.md`

这条入口的核心意义是：

**从研究一条 thesis，升级到比较多个 thesis。**

---

### 用法三：source bundle 一键流水线

适合：

- 手上已经有一批原始材料
- 不想手动先整理成最终 pack JSON
- 想从材料直接跑到研究包

脚本：

`scripts/run_source_pipeline.py`

示例输入：

`examples/source_bundle_input.json`

输出分两层：

#### 第一层：草稿输入

目录：

`01_draft/`

产物：

- `draft_pack_input.json`
- `extraction_report.json`

这一层做的事：

- 从 source bundle 里抽 evidence
- 抽 signal
- 抽 quote snippet
- 给 source 打 confidence
- 给 evidence 补 link reason
- 给公司补初始评分字段

#### 第二层：最终研究包

目录：

`02_final_pack/`

产物：

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

这条链路最重要的地方在于：

**它已经不只是一个会回答问题的 skill，而是一个会整理研究证据、沉淀研究包的流水线。**

---

## 它和普通“问 AI 买什么”有什么不同

普通玩法是：

- 问 AI 哪只票好
- 问 AI 帮我总结一下
- 问 AI 这个赛道有没有机会

这个产品不这么干。

它的顺序是：

1. 先定系统
2. 再画栈
3. 再找瓶颈
4. 再拉证据
5. 最后才给方向、公司和优先级

差别就在这里：

**它不是让 AI 代替你拍脑袋，而是让 AI 帮你把研究流程做扎实。**

---

## 现在这版最有价值的地方

我觉得当前版本最值钱的是这 4 点：

### 1. 结构统一

不管是单条 thesis，还是多条 lane，对外输出格式都比较统一。

### 2. 证据不再只是摘要

现在已经能保留：

- quote snippet
- source confidence
- link reason

也就是开始有“证据链”的味道了。

### 3. 图谱已经能落地

现在不只是写文字，还能输出：

- `graph.json`
- `graph.mmd`
- `graph_mermaid.md`

后面做可视化会轻松很多。

### 4. 已经能比较优先级

不只是分析一条线，而是能比较多条线的研究价值。

---

## 它适合谁

适合：

- 想认真研究 AI 基础设施的人
- 想把投研流程交给 Agent 的人
- 想把零散材料变成结构化研究的人
- 想做长推、信息图、研究 memo 底稿的人

不太适合：

- 只想直接抄股票代码的人
- 只看情绪和热度的人
- 想让 AI 替自己做短线决策的人

---

## 现在还没做完的地方

这版已经很像一个产品了，但还没有完全做满。

目前最值得继续补的两块是：

### 1. 更细的证据抽取

比如：

- 发布时间
- 域名来源
- claim 类型
- quote offset

### 2. 图谱和证据联动

也就是在图上直接点到证据原句和出处。

这两块一补上，产品感会更强。

---

## 最后一句

Chokepoint Atlas 现在不是一个“给我几个代码”的 prompt。

它更像一个：

**把 AI 叙事拆成真实供应链，再把真实供应链整理成研究证据和交付物的产品。**
