# Chokepoint Atlas 2.0 - 产品规划与落地任务书

## 先讲结论

`Chokepoint Atlas 1.0` 已经证明了一件事：

它能把一个大赛道拆开，找到真正可能卡脖子的地方。

但 1.0 还是更像一个“研究方法 skill”，不是一个“能交付研究结果的产品”。

所以 2.0 的目标，不是单纯多加一点提示词，也不是让它“更会报票”。

2.0 要解决的是更实际的问题：

1. 用户给一个赛道之后，系统能不能稳定产出结构化研究包
2. 研究里的每个关键判断，能不能标清证据强弱
3. 公司、部件、催化剂之间，能不能形成可复用的关系图
4. 最后能不能给出一个清晰的研究优先级，而不是只写一段好看的分析

一句话说：

**1.0 是研究动作，2.0 要变成研究产品。**

---

## 一、1.0 目前已经有的能力

### 1.0 已经能做什么

- 从终端系统出发拆供应链
- 画 6-9 层栈
- 找物理 / 认证 / 产能瓶颈
- 先给方向，再给名字
- 区分执行者、瓶颈纯度和早期 optionality

### 1.0 还不够产品化的地方

- 新闻、研报、财报还只是“参考”，不是结构化证据
- 公司之间的关系主要靠文字描述，没有图谱产物
- 输出更像分析过程，不像可以直接沉淀、复盘、分享的研究包
- 缺少统一打分系统，很难比较“这条线现在更值得深挖，还是另一条线更值得深挖”
- 缺少本地脚本入口，不方便别人直接跑一个 demo

---

## 二、2.0 要做成什么产品

### 产品定位

`Chokepoint Atlas 2.0` 是一个 **AI 基础设施瓶颈研究系统**。

它接收一个结构化主题输入，然后吐出一整套可复用研究包：

- `Quick Scan`
- `Evidence Memo`
- `Graph JSON`
- `Scorecard`
- `Catalyst Watch`

它不再只是回答：

- 下一个瓶颈在哪

还要回答：

- 这个判断的证据硬不硬
- 关键关系怎么连
- 这条线现在该不该排进高优先级
- 哪些名字只是线索票，哪些名字是更扎实的执行者

---

## 三、2.0 的产品形态

### 形态 A：Agent Skill

这是现在已经存在的形态。

适合：

- 对话式研究
- 长推文 / memo 起草
- 把方法论交给别的 Agent

### 形态 B：本地脚本 MVP

这是本轮开始补的形态。

适合：

- 输入一个结构化案例
- 直接在本地生成研究包
- 做 demo、做交付、做信息图底稿
- 给别的 Agent / 研究员一个可复用的最小工作流

### 形态 C：后续可以继续做的轻量应用层

暂时不急着上 UI，但 2.0 的脚本层要先按未来产品来设计。

后续可以扩成：

- lane watch dashboard
- graph viewer
- catalyst tracker
- 多赛道比较器

---

## 四、2.0 的核心模块

### 模块 A：Evidence Engine

目标：

把所有原始材料做证据分层，而不是混着看。

证据分四类：

- A 类：硬证据
  - 10-K / 10-Q / 年报 / 季报
  - earnings call
  - investor presentation
  - 官方 supplier / partner / customer 披露

- B 类：半硬证据
  - 主流行业媒体
  - conference / fireside chat
  - sell-side 研报摘要
  - 产品手册、招标材料

- C 类：弱证据
  - X / Reddit / forum / KOL 总结

- D 类：待验证
  - 传闻
  - 无原始出处截图
  - 只有转述、没有原文

每条关键判断都要有明确标签：

- `Confirmed`
- `Inferred`
- `Weak`
- `Needs verification`

---

### 模块 B：Graph Engine

目标：

把“列公司”升级成“画关系”。

最小支持 5 类节点：

- 终端系统
- 部件 / 功能层
- 公司
- 证据
- 催化剂

最小支持 6 类边：

- `supplies`
- `depends_on`
- `competes_with`
- `confirmed_by`
- `likely_benefits_from`
- `catalyzed_by`

输出至少要能生成：

- `graph.json`
- 一张文字版 `Graph Card`

---

### 模块 C：Signal Engine

目标：

不是只摘要财报，而是把财报、新闻、研报里的“方向信号”抓出来。

信号词典的第一批关键词：

- demand > supply
- qualification
- design win
- booked out
- allocation
- ramp
- lead time
- sole source
- dual source
- bottleneck
- constrained
- pilot
- commercialization
- mass production
- yield improvement

这些信号最终要映射成 6 个判断维度：

- 需求强度
- 供给约束
- 认证进展
- 放量临界点
- 竞争格局变化
- 管理层信心

---

### 模块 D：Scoring Engine

目标：

让“值得研究”这件事可以比较，而不是凭感觉。

先做 5 个基础分：

1. `Constraint Score`
2. `Evidence Score`
3. `Consensus Score`
4. `Mispricing Score`
5. `Catalyst Score`

最后输出两类结果：

- `Lane Score`
- `Name Score`

重点不是装作精确，而是让优先级更稳定。

---

### 模块 E：Output Engine

2.0 必须不是一种输出打天下。

第一阶段支持 5 种输出：

1. `Quick Scan`
2. `Evidence Memo`
3. `Graph Card`
4. `Scorecard`
5. `Catalyst Watch`

---

## 五、产品 MVP：这次先把什么真的做出来

这次不追求把 2.0 一口气做满。

先把最小可用产品跑通。

### MVP 目标

用户给一个结构化 JSON 输入，脚本自动生成：

- `research_pack.json`
- `quick_scan.md`
- `evidence_memo.md`
- `graph.json`
- `graph_card.md`
- `scorecard.json`
- `catalyst_watch.md`

### MVP 的意义

这一步一旦跑通，Chokepoint Atlas 就不再只是“一个 skill 描述文档”。

它已经是一个：

- 有输入格式
- 有固定输出格式
- 能沉淀研究包
- 能交给别的 Agent 接着跑

的产品底座。

---

## 六、MVP 的输入输出约定

### 输入

先用结构化 JSON。

最小字段包括：

- `meta`
- `thesis`
- `stack_layers`
- `bottlenecks`
- `evidence`
- `companies`
- `catalysts`

### 输出目录

建议统一生成到：

`out/<pack_id>/`

例如：

`out/nvidia-dsx-ai-factory-demo/`

---

## 七、脚本层设计

### 脚本 1：`scripts/build_research_pack.py`

职责：

- 读取结构化输入
- 标准化证据标签
- 计算 lane / name priority
- 组装 graph schema
- 生成 markdown / json 输出包

这是 2.0 的第一个产品化入口。

### 示例输入：`examples/ai_factory_lane_input.json`

职责：

- 提供一个能直接跑通的 demo
- 演示 AI Factory / HBM 测试 / 先进封装这条线怎么结构化表达

---

## 八、用户真实会怎么用

### 用法 1：做 demo

```bash
python3 scripts/build_research_pack.py \
  --input examples/ai_factory_lane_input.json \
  --output out/ai_factory_demo
```

### 用法 2：研究员自己改 JSON

研究员先把赛道假设、证据和公司关系整理进 JSON，再交给脚本生成研究包。

### 用法 3：Agent 先研究，再落地成 pack

先用 Skill 做开放式研究，再把沉淀出来的结果落成标准化输入，交给脚本生成统一交付物。

---

## 九、第一阶段验收标准

MVP 做完以后，至少要满足这几个标准：

1. 输入一个 demo JSON，能稳定生成完整研究包
2. 每条证据都能自动落到四级标签之一
3. graph 输出不是空壳，要有节点、边、证据、催化剂
4. lane score 和 name score 有明确来源，不是随便凑数
5. markdown 输出是人能直接看、能直接继续改的

当前进度补充：

- 已完成结构化输入校验，输出 `validation_report.json`
- 已完成 `graph.json -> Mermaid` 转换，输出 `graph.mmd / graph_mermaid.md`
- 已完成多 lane 横向比较脚本，输出 lane ranking 和 compare memo

---

## 十、第二阶段怎么继续迭代

MVP 跑通之后，再补这些：

1. 新闻 / 财报 / 研报抽取器
2. 催化剂时间轴可视化
3. lane 对 lane 的批量比较
4. graph 可视化渲染
5. 特定赛道模板
   - AI Factory
   - 光互联
   - 先进封装
   - 电力与液冷
   - 人形机器人

---

## 十一、版本切分建议

### 1.1

把 1.0 从“纯 Skill”升级成“Skill + 本地脚本 MVP”。

这是这一轮要完成的目标。

### 2.0

在 1.1 的基础上，把证据抽取、关系图、优先级、催化剂跟踪全部做稳定。

### 3.0

如果未来真要做成可视化应用，再考虑 dashboard / UI。

---

## 十二、产品总结

Chokepoint Atlas 2.0 不是一个“更会找票”的 skill。

它是一个把：

- 新闻
- 财报
- 研报
- 关系图
- 优先级
- 催化剂

揉在一起，用来验证 AI 基础设施瓶颈的研究系统。

如果 1.0 的关键词是：

**提问**

那么 2.0 的关键词就是：

**证据、关系、优先级、交付物。**
