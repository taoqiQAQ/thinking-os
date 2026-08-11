# Thinking OS Skill v2.0

[English](README.md) | [中文](README.zh-CN.md)

Thinking OS 是一个可移植的 [Agent Skill](https://agentskills.io/)，用于将复杂任务路由到最少但足够有效的推理、证据、挑战、决策状态和行动机制。它是一个推理路由器，而不是一条巨型提示词。

## 它能做什么

Thinking OS 帮助 Agent 判断：

1. 是否需要结构化推理；
2. 推理应该深入到什么程度；
3. 应该使用哪些最少且必要的推理模型；
4. 是否需要最新、私有、本地或代码仓库中的证据；
5. 对抗性复盘是否有实际价值；
6. 什么时候应该停止思考并采取下一步行动。

对于简单任务，它会刻意避免使用过重的框架，也不会暴露私有思维链。

## 中文日常使用说明书

如果你想了解 Thinking OS 的日常使用方式，可以直接在 GitHub 阅读 [Thinking OS v2.0.0 Stable 中文日常使用说明书](docs/Thinking%20OS%20v2.0.0%20Stable.md)。

## 仓库内容

本仓库是 **v2.0.0 生产运行包**，包含使用该 skill 所需的文件：

```text
SKILL.md                 # Skill 入口和路由器
references/              # 详细策略、模型、领域和协议
scripts/                 # 运行时辅助引擎
state/                   # 决策状态 JSON schema
docs/                    # 面向使用者的指南和文档
ARCHITECTURE.md          # 系统架构
INSTALL.md               # 安装说明
SECURITY.md              # 数据与安全边界
RELEASE.md               # 发布状态和离线校验门槛
CHANGELOG.md             # 版本历史
MANIFEST.json            # 文件清单与哈希
```

生产包刻意排除了仅用于开发的评测套件、基准测试样例、生成的运行结果和发布工具。这些资产不是运行时所必需的。

## 安装

克隆本仓库，并保留目录名 `thinking-os`：

```bash
git clone https://github.com/taoqiQAQ/thinking-os.git
```

将 `thinking-os` 文件夹复制到你的 Agent-Skills 兼容宿主所支持的 Skills 目录中。该文件夹的顶层必须包含 `SKILL.md`。

发布压缩包 `thinking-os-skill-v2.0.0.zip` 使用相同的目录布局，并带有一个 `thinking-os/` 外层目录。

## 调用方式

通常可以让宿主自动激活该 skill。你也可以直接说：

- `Use thinking-os for this decision.`
- `Use thinking-os /red on this plan.`
- `Use thinking-os /action; stop analyzing and give me the execution path.`

支持的模式覆盖参数包括 `/fast`、`/deep`、`/max`、`/red`、`/first`、`/data`、`/idea`、`/action` 和 `/simple`。

## 校验

运行时辅助引擎只使用 Python 标准库。在仓库根目录执行：

```bash
python3 -m py_compile scripts/decision_state.py scripts/improvement_engine.py
```

v2.0.0 已通过离线回归校验。实时 A/B 质量或工具使用效果证明需要单独授权的运行，本软件包不对此作出声称。

## 设计原则

- 只有当思考能改善决策时才进行思考。
- 只有当信息可能改变决策时才进行研究。
- 只有当挑战能够降低有意义的风险时才进行挑战。
- 当现实行动能带来比继续分析更多的信息时，就开始行动。
- 除非宿主提供持久化存储，否则永远不要声称具备跨会话持久化能力。
- 永远不要将自我改进变更静默地升级为生产规则。

请参阅 [`SKILL.md`](SKILL.md) 了解运行时入口，参阅 [`ARCHITECTURE.md`](ARCHITECTURE.md) 了解完整设计。

## 许可证

本项目采用 [MIT License](LICENSE) 开源。
