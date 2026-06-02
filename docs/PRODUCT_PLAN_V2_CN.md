# Chokepoint Atlas 2.0 - 产品规划

## 一句话定义

Chokepoint Atlas 1.0 是一个会拆赛道、找瓶颈的研究 skill。  
Chokepoint Atlas 2.0 要升级成一个会拉证据、会画关系、会排优先级的研究系统。

它不只是回答：

- 下一个 AI 基础设施瓶颈在哪

还要回答：

- 这个瓶颈的证据到底硬不硬
- 哪些公司、项目、零件、催化剂彼此强依赖
- 这条线应该不应该排进当前研究优先级

## 1.0 的能力边界

1.0 已经能做的事：

- 从终端系统出发拆供应链
- 画 6-9 层栈
- 找物理 / 认证 / 产能瓶颈
- 先给方向，再给名字
- 区分执行者和早期可选性

1.0 的问题也很明显：

- 新闻、研报、财报还只是“参考材料”，不是结构化证据
- 公司之间的关系主要靠文字描述，没有图谱
- 对“这条线很热”和“这条线证据更硬”区分不够
- 缺少明确的优先级打分系统
- 缺少催化剂时间轴和持续跟踪能力

## 2.0 的升级目标

2.0 要完成四个升级：

1. 从“找瓶颈”升级到“验证瓶颈”
2. 从“列公司”升级到“画关系”
3. 从“看故事”升级到“看证据等级”
4. 从“写分析”升级到“排研究优先级”

## 2.0 的核心模块

### 模块 A：Evidence Engine

把所有输入材料做证据分层，而不是混着看。

建议分为四类：

- A 类：硬证据
  - 10-K / 10-Q / 年报 / 季报
  - earnings call
  - investor presentation
  - 官方 supplier / partner / customer 披露

- B 类：半硬证据
  - 主流行业媒体
  - sell-side 研报摘要
  - conference / fireside chat
  - 招股书、招标文件、产品手册

- C 类：弱证据
  - X 推文
  - Reddit / forum
  - KOL 总结
  - 二手笔记

- D 类：待验证
  - 传闻
  - 无原始出处截图
  - 只有转述、没有原文的消息

每一条重要判断，都应该自动打上：

- Confirmed
- Inferred
- Weak
- Needs verification

### 模块 B：Graph Engine

把赛道分析从“列表思维”升级成“图谱思维”。

建议支持 5 类节点：

- 终端系统
  - GB300 NVL72
  - TPU pod
  - Optimus
  - AI factory

- 部件 / 功能层
  - 激光器
  - InP 衬底
  - 光模块
  - 谐波减速器
  - 液冷
  - 配电

- 公司
  - supplier
  - customer
  - foundry
  - competitor
  - test vendor

- 证据
  - 财报原句
  - 新闻
  - 研报观点
  - 供应商名单变化

- 催化剂
  - 财报日
  - 扩产公告
  - 认证完成
  - 量产节点

建议支持 6 类边：

- supplies
- depends_on
- competes_with
- confirmed_by
- likely_benefits_from
- catalyzed_by

### 模块 C：Signal Engine

从财报、新闻、研报里提取“有方向意义的信号”，而不是只做摘要。

建议建立信号词典：

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

这些信号最后映射成 6 个维度：

- 需求强度
- 供给约束
- 认证进展
- 放量临界点
- 竞争格局变化
- 管理层信心

### 模块 D：Scoring Engine

2.0 需要一个简单但稳定的优先级系统。

建议至少打 5 个分：

1. Constraint Score
2. Evidence Score
3. Consensus Score
4. Mispricing Score
5. Catalyst Score

最后输出两类分数：

- Lane Score
- Name Score

目标不是机械化选股，而是帮助你决定：

- 下一条该深挖哪条线
- 哪家公司值得进一步验证

### 模块 E：Output Engine

2.0 不该只有一种输出。

建议支持 4 种：

1. Quick Scan
   - 一句 thesis
   - 一张栈
   - 一个瓶颈
   - 三个该查的证据

2. Evidence Memo
   - 完整分析
   - 带证据等级
   - 适合长推 / 文档

3. Graph Card
   - 一张关系图
   - 一段结论
   - 适合图文 / 信息图

4. Catalyst Watch
   - 财报
   - 认证
   - 量产
   - 扩产
   - 客户导入

## 用户会直接感知到的升级

从用户视角，2.0 应该有这几个明显变化：

1. 不再只是“给方向”
   - 还会告诉你这个方向的证据强弱

2. 不再只是“给公司名单”
   - 还会给出这些公司和终端系统之间的关系图

3. 不再只是“讲逻辑”
   - 还会明确哪些地方已经确认，哪些只是推断

4. 不再只是“一次性分析”
   - 还可以做催化剂跟踪

## 推荐的仓库结构升级

建议新增这些文件：

- `references/evidence-ladder.md`
- `references/graph-schema.md`
- `references/scoring-framework.md`
- `references/catalyst-watch.md`
- `references/output-formats-v2.md`

后续如果需要更进一步，可以再加：

- `assets/graph-templates/`
- `scripts/build_graph_json.py`
- `scripts/score_lane.py`

## 第一阶段落地范围

建议先做 2.0 的第一阶段，不要一次做太满。

第一阶段只做三件事：

1. 证据标签化
   - Confirmed / Inferred / Weak / Needs verification

2. 关系图 schema
   - 节点、边、最小可用图结构

3. 打分框架
   - 给 lane 和 name 一个清晰的优先级输出

这三个一完成，2.0 就已经和 1.0 拉开差距了。

## 第二阶段落地范围

第二阶段再补：

1. 催化剂时间轴
2. 图谱输出模板
3. 简单脚本化
4. 针对特定赛道的预设模板

## 产品总结

Chokepoint Atlas 2.0 不是一个“更会找票”的 skill。

它是一个把：

- 新闻
- 研报
- 财报
- 公司关系
- 催化剂时间轴

揉在一起，用来验证 AI 基础设施瓶颈的研究系统。

如果 1.0 的关键词是：

**提问**

那 2.0 的关键词就是：

**证据、关系、优先级。**
