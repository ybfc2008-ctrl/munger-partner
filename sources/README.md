# 来源登记与证据等级

`source-manifest.csv` 是资料入口账本，不是观点真伪清单。来源通过登记，只代表第三方可以找到同一材料；由它提取的知识单元仍必须从 Candidate 开始。

## 证据等级

- **A-primary**：公司、学校、节目制作方或作者本人发布的原始文件、录音或录像。
- **B-traceable-transcript**：能回到原始事件或录音的全文转录；允许轻微清理，但必须记录编辑者。
- **C-named-notes**：有署名记录者的参会笔记或摘要。可用于发现线索，不能直接称为逐字原话。
- **D-lead**：书籍、译本、转载、无可靠来源链的文本。只用于寻找更好的来源。

## 发布规则

- `link_and_excerpt`：公开仓库只保存来源链接、定位信息和必要短引文，不重新发布完整文件。
- `metadata_only`：只登记书目和来源，不复制正文或大段摘录。
- 没有明确许可证时，一律不把 Drive 中的 PDF、EPUB、录音或视频提交到 GitHub。

## 当前结论

1. 伯克希尔 2014 年报已定位到公司官网，芒格正文位于报告第 39 页起。
2. 1995 年演讲找到 Whitney Tilson 转录的 21 页可搜索版本，但仍属于 B 级；Drive 版本需要 OCR。
3. 2020、2021、2023 Daily Journal 已定位到 CNBC 或 Yahoo Finance 的原始发布视频。
4. 1999–2011 Wesco 主要是 Whitney Tilson、Peter Boodell 等人的署名笔记，统一保持 C 级。
5. Munger Archive 可作为发现和纠错索引，但它明确是非官方项目，不替代原始来源。

## 维护方式

每次新增资料，先加入 manifest，再运行：

```bash
python3 scripts/validate_sources.py
```

`next_action` 清空前，不得把来源标为 `ready_candidate`。`ready_candidate` 也只代表可以开始提取候选条目。
