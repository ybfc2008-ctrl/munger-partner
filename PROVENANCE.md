# 设计来源与独立性

## 参考项目

### SocialAI Tianji

- 项目：https://github.com/SocialAI-tianji/Tianji
- 借鉴方向：中文人际场景的上下文敏感性；Prompt、Agent、知识库、数据制造与清洗分层；垂直领域应用的工程化组织。
- 未采用：其具体语料、提示词、训练数据和源代码。

### Poor Charlie's Almanack Skill

- 项目：https://github.com/kangarooking/poor-charlies-almanack-skill
- 借鉴方向：把判断拆成可组合模块；Candidate、Verified、Rejected 审计链；反向验证与压力测试。
- 未采用：其书籍摘录、生成候选、具体 Skill 文本和源代码。

## 本项目的原创组合

“Munger Partner”将证据纪律、少模型原则与关系语境合并为三层信任：

1. **关系信任**：先理解人的处境，不用聪明压过人。
2. **判断信任**：主动寻找反证和失败路径，不迎合既定答案。
3. **证据信任**：原话、事实、推断、建议分层，并保留可审计状态迁移。

任何未来引入的第三方内容都必须单独记录来源、许可证和允许的使用范围。
