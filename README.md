# Munger Partner

> 重要决定之前，先问问你的合伙人

一个中文优先、证据可追溯的开源 AI Skill：用芒格式判断工具帮助人减少重大错误，但不扮演芒格，不制造语录，也不把冷冰冰的模型压在人身上。

## 它有什么不同

- **先理解人，再分析事**：支持陪伴、判断、求证、语料审查四种工作方式。
- **事实与推断分层**：原话、外部事实、框架推断、行动建议不得混写。
- **少模型原则**：一次只用真正改变结论的一至三个模型。
- **逆向生产系统**：所有语料先进入 Candidate，由独立审查后才能成为 Verified。
- **保留失败轨迹**：Rejected 条目与原因不会被删除，防止换名字重新混入。
- **适合 GitHub 协作**：内置来源纠错 Issue、Pull Request 检查和零依赖校验脚本。

## 仓库结构

```text
munger-partner/
├── RULES.md                      # 最高规则
├── skill/munger-partner/         # 可安装 Codex Skill
├── raw/                          # L0：不可变原始证据或其指纹
├── corpus/                       # L1：原文、中文、出处与定位
├── candidates/                   # AI 候选，不可直接引用
├── verified/                     # 独立审查通过
├── rejected/                     # 拒绝条目及理由
├── models/                       # L2：最小核心模型集合
├── cases/                        # L3：失败案例优先，多对多映射
├── decision-engine/              # L4：逆向决策流程
├── index/                        # 派生检索索引，可重建
├── sources/                      # Drive 与公开来源登记表
├── reviews/                      # 独立逆向审查记录
├── schemas/                      # Metadata 规范
├── scripts/                      # 来源、语料与 Skill 校验
└── .github/                      # 协作与纠错入口
```

## 快速使用

### 作为 Codex Skill

把 `skill/munger-partner` 复制到你的 Codex skills 目录，然后调用：

```text
$munger-partner 我在考虑一项不可逆的职业选择，帮我先找失败路径。
```

也可以直接使用发布包中的 `munger-partner.skill`。

### 校验语料

本项目只依赖 Python 标准库：

```bash
python3 scripts/validate_sources.py
python3 scripts/validate_corpus.py
```

知识单元是带 JSON frontmatter 的 Markdown。复制 `templates/knowledge-unit.md` 创建候选条目；只有通过独立逆向审查并补齐 Verified 字段后，才可移动到 `verified/`。

审查者使用 `templates/review.md`，将结论写入 `reviews/`。`verify` 只是升级建议；生产者仍须确认所有 Verified 硬条件并保留审查者身份。

所有资料先登记在 [`sources/source-manifest.csv`](sources/source-manifest.csv)。它区分官方原件、可回查转录、署名笔记和二手线索；来源登记通过不等于知识条目已经验证。

首个 1994 USC MVP 的范围、审查轨迹、北极星指标和剩余缺口见 [`MVP-1994-USC.md`](MVP-1994-USC.md)。

## 重要声明

本项目不是查理·芒格本人、遗产管理方或任何相关机构的官方产品。“芒格”描述的是公开思想启发的判断框架，不代表本人对新事件的观点。投资、法律、医疗等高风险问题需要独立核验和合格专业意见。

## 参考与来源

工程上参考了 [SocialAI Tianji](https://github.com/SocialAI-tianji/Tianji) 的垂直领域数据、知识库与场景化路线，以及 [Poor Charlie's Almanack Skill](https://github.com/kangarooking/poor-charlies-almanack-skill) 的原子化判断模块、Candidate/Rejected 审计和压力测试思路。本仓库是独立实现，没有复制两者的代码或语料。详见 [PROVENANCE.md](PROVENANCE.md)。

## 贡献与许可证

请先阅读 [RULES.md](RULES.md) 和 [CONTRIBUTING.md](CONTRIBUTING.md)。发现错误归因或断章取义时，请使用“来源纠错”Issue 模板。

代码与原创文档采用 [MIT License](LICENSE)。导入语料仍受各自原始版权与许可约束；MIT 不会自动赋予第三方文本的再分发权。
