# 英伟达 AI Factory 产业地图 - GPT Image 中文提示词

## 推荐模型参数

- model: `gpt-image-2`
- size: `2048x1152`
- quality: `high`
- ratio: `16:9`

## 主提示词

请生成一张 **中文信息图版产业地图**，主题是：

**《英伟达 AI Factory 产业地图》**

画面风格参考英伟达 GTC 主题演讲大屏，但不要直接复刻演讲截图。  
整体视觉要像一张高端、冷静、克制、信息密度高的 B2B 科技产业地图。

### 画面要求

- 16:9 横版信息图
- 深色背景，黑色 + 深蓝色为主
- 点缀色使用低饱和荧光绿、青蓝、电光紫
- 版式要像顶级科技咨询图 + NVIDIA keynote 风格
- 清晰、专业、克制，不要卡通，不要花哨
- 不要做成宣传海报，要做成真正的信息图
- 不要使用真实公司 logo，统一用简洁文字标签代替
- 文字必须是简体中文，尽量清晰可读
- 尽量减少长段正文，用模块标题 + 短标签 + 箭头关系

### 核心结构

整张图做成 **7 层纵向产业地图**，从上游到底层应用，层与层之间有清晰箭头关系。

标题区域：

- 主标题：**英伟达 AI Factory 产业地图**
- 副标题：**从芯片、机柜、园区、电力冷却到 AI 云服务的全栈关系**

中间主体用 7 层堆叠结构，每层一个独立横向模块，模块之间用细箭头和连接线表示上下游关系。

### 七层模块内容

#### L0 上游芯片与关键零部件

赛道标签：
- 半导体
- 先进封装
- 高速互连
- 电力器件
- 冷却零部件

关键词：
- GPU / CPU / DPU / NIC
- HBM
- 光模块
- 电源器件
- 冷板 / 泵 / CDU

代表公司标签示意：
- NVIDIA
- TSMC
- SPIL
- Kinsus
- KYEC

#### L1 计算系统

赛道标签：
- OEM
- ODM
- 服务器整机
- 机柜级系统集成

关键词：
- AI 服务器
- Rack-scale system
- 主板
- 电源
- 散热

代表公司标签示意：
- Dell
- HPE
- Lenovo
- Supermicro
- Foxconn
- QCT
- Wiwynn

#### L2 基础设施与园区

赛道标签：
- 数据中心
- 园区开发
- Land / Power / Shell
- Colocation

关键词：
- 机房
- 园区
- 电力接入
- 上架环境
- 交付容量

代表公司标签示意：
- AirTrunk
- Digital Realty
- Equinix
- NTT
- STT GDC

#### L3 电力与冷却

赛道标签：
- 配电
- UPS
- HVAC
- 液冷
- 电网互动

关键词：
- 配电
- 变压
- UPS
- 液冷
- 热管理
- PUE

代表公司标签示意：
- Eaton
- Schneider
- Vertiv
- Trane
- Delta
- GE Vernova

#### L4 设计与施工

赛道标签：
- AEC
- BIM
- PLM
- 仿真
- 数字孪生

关键词：
- 园区设计
- 热仿真
- 电力仿真
- 施工协同
- 数字孪生

代表公司标签示意：
- Cadence
- Siemens
- Dassault
- Bentley
- Jacobs
- PTC

#### L5 AI 工厂软件

赛道标签：
- 集群调度
- 生命周期管理
- 存储编排
- 运维智能
- 功耗优化

关键词：
- 多租户
- 调度
- 存储
- 运维
- GPU 利用率
- 功耗优化

代表公司标签示意：
- Mirantis
- OpenNebula
- Red Hat
- Rafay
- WEKA
- VAST
- Phaidra

#### L6 AI 云服务

赛道标签：
- GPU Cloud
- Sovereign AI
- Training Cloud
- Inference Cloud

关键词：
- 训练算力
- 推理算力
- 企业 AI
- 主权 AI
- token 成本

代表公司标签示意：
- CoreWeave
- Lambda
- Nebius
- Nscale
- Yotta
- Firmus

### 关系表达

图中必须明确表达两条关系线：

#### 1. 物理产业链

从上到下或从左到右清楚展示：

**上游芯片与关键零部件 -> 计算系统 -> 基础设施与园区 -> AI 云服务**

同时让：

**电力与冷却** 作为支撑层连接 **基础设施与园区** 和 **AI 云服务**

#### 2. 控制与设计链

让：

- 设计与施工
- AI 工厂软件

以侧向连接线的方式，连接到：

- 计算系统
- 基础设施与园区
- 电力与冷却
- AI 云服务

形成“设计 / 调度 / 运维”控制链。

### 右侧结论框

在画面右侧做一个简洁高端的总结框，标题：

**核心结论**

内容用 4 条短句：

- AI Factory 竞争不再只是抢 GPU
- 真正的门槛变成整座工厂的交付能力
- 电力、冷却、园区和软件开始与算力同等重要
- 谁能更快让 AI Factory 落地，谁就能吃到下一阶段红利

### 底部小结

底部做一行短总结：

**从芯片到云，不是单点竞争，而是一整座 AI 工厂的系统竞争**

### 视觉限制

- 不要照片拼贴
- 不要人物
- 不要演讲台
- 不要真实 logo 墙
- 不要过多装饰光效
- 不要把文字做得太小
- 不要密密麻麻塞满整张图
- 不要像营销海报，要像战略地图

## 稳妥版补充约束

如果模型对中文小字表现不稳定，请优先保证：

1. 标题清晰
2. 七层结构清晰
3. 每层 3-5 个关键词清晰
4. 箭头关系清晰
5. 右侧结论框清晰

宁可减少公司标签数量，也不要让画面文字糊掉。

## CLI 生成命令

如果本地已经配置 `OPENAI_API_KEY`，可以直接运行：

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/.system/imagegen/scripts/image_gen.py"

python "$IMAGE_GEN" generate \
  --model gpt-image-2 \
  --quality high \
  --size 2048x1152 \
  --prompt-file /Users/windows/Desktop/ai-bottleneck-hunter-repo/docs/DSX_AI_FACTORY_INFOGRAPHIC_PROMPT_CN.md \
  --out /Users/windows/Desktop/dsx-ai-factory-infographic-cn.png
```
