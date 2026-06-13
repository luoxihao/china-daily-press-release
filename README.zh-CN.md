# China Daily press release skill

语言：[English](README.md) | 中文

这是 `china-daily-press-release` 技能的用户说明。这个技能帮助 Codex 和 Claude Code 起草、改写、润色、审校和事实核查英文对外传播稿件，写作风格参考公开 China Daily 文章中可迁移的倾向。

它不是 China Daily 官方工具，也不能声称稿件由 China Daily 发布、审核、授权、背书或认可。公开 China Daily 文章只能作为风格研究来源；这个技能不保存、复用或改写完整文章文本。

## 用途

你可以在这些场景中使用：

- 根据已核实的中文或英文材料起草英文通稿。
- 把中文宣传材料改写成英文新闻稿，而不是逐句直译。
- 生成中英双语稿，并检查两种语言中的事实是否一致。
- 润色已有英文稿，让语气更像克制的新闻稿。
- 审核事实缺口、未证实说法、宣传腔、中文式英语和 AI 腔。
- 生成标题备选、导语备选、事实核查说明、编辑说明或待确认清单。

适合的材料包括：

- 地方政府或机构活动通稿。
- 文旅活动、城市推广、论坛、展会和节庆活动。
- 体育赛事、马拉松、交流项目和文化遗产报道。
- 需要做风格审校和事实核查的英文初稿。

不适合的任务：

- 仿写、改写或贴近某一篇具体 China Daily 文章。
- 编造事实、引语、职务、机构、奖项、日程、数据或官方名称。
- 生成广告文案、口号、宣传册式文字或无法核实的形象包装。
- 暗示 China Daily 写作、审核、认可、背书或发布了稿件。

## 快速使用

在 Codex 或 Claude Code 中，直接用技能名调用：

```text
$china-daily-press-release 请根据以下已核实的中文材料写一篇英文对外传播新闻稿，并附上事实核查清单和待确认信息。
```

审校已有英文稿：

```text
$china-daily-press-release 请审校下面这篇英文稿，重点检查事实风险、未证实说法、宣传语气、中文式英语、AI 腔和是否适合国际读者。
```

生成中英双语稿：

```text
$china-daily-press-release 请把以下中文材料改写成英文新闻稿，再给出中文版本，并检查中英事实是否一致。
```

如果材料不足，技能应该输出事实缺口和安全的稿件框架，而不是补写未经确认的信息。

## 它是怎么实现的

agent 读取的主入口是 `SKILL.md`。其中的 frontmatter 定义了技能名和触发描述：

```yaml
name: china-daily-press-release
description: Use this skill when the user asks to write, translate, edit, polish, fact-check, localize, or review English press releases...
```

如果你希望 `$china-daily-press-release` 继续可用，请不要修改 `name: china-daily-press-release`。`README.md` 和 `README.zh-CN.md` 只是用户说明，不控制技能名。

技能目录由这些部分组成：

- `SKILL.md`：给 agent 看的说明，定义适用场景、事实优先流程、版权边界、输出结构和质量检查。
- `references/`：写作规则、事实核查流程、风格清单、短语规则、公开文章风格笔记和 docx 规则摘要。
- `templates/`：英文通稿、双语稿、文旅活动、体育赛事、文化遗产、事实核查报告和编辑说明的结构模板。
- `examples/`：示例调用、输出结构示例和审校示例。
- `scripts/`：用于规则提取、样本分析和机械检查的辅助脚本。
- `agents/`：agent 配置文件。

基本流程是：

1. 识别任务类型：起草、改写、润色、审校、事实核查、标题备选、导语备选或编辑说明。
2. 从材料中提取事实清单：活动名称、时间、地点、主办方、人物、数字、引语、背景和不确定项。
3. 把事实分为已确认、需要来源、存在冲突、缺失和不宜使用。
4. 选择最接近的模板。
5. 只用已确认事实起草或修改稿件。
6. 根据任务需要做风格检查、事实检查和中英一致性检查。

这个设计主要降低三类风险：补写事实、语气过度宣传、输出过度接近某一篇公开文章。

## 在 Codex 上安装

Codex 的个人技能通常放在：

```text
~/.agents/skills/
```

请在包含源码仓库文件夹 `china-daily-press-release-skill` 的父目录中运行命令。

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills\china-daily-press-release" | Out-Null
Copy-Item -Recurse -Force ".\china-daily-press-release-skill\*" "$env:USERPROFILE\.agents\skills\china-daily-press-release"
```

### macOS

```bash
mkdir -p ~/.agents/skills
mkdir -p ~/.agents/skills/china-daily-press-release
cp -R ./china-daily-press-release-skill/. ~/.agents/skills/china-daily-press-release/
```

### Linux

```bash
mkdir -p ~/.agents/skills
mkdir -p ~/.agents/skills/china-daily-press-release
cp -R ./china-daily-press-release-skill/. ~/.agents/skills/china-daily-press-release/
```

安装后开启新的 Codex 会话，然后调用：

```text
$china-daily-press-release 请根据这份材料写一篇英文新闻稿。
```

如果 Codex 没有找到技能，请检查：

- 目录是否为 `~/.agents/skills/china-daily-press-release/`。
- `SKILL.md` 是否在该目录第一层。
- frontmatter 是否仍包含 `name: china-daily-press-release`。

## 在 Claude Code 上安装

Claude Code 的个人技能通常放在：

```text
~/.claude/skills/
```

请在包含源码仓库文件夹 `china-daily-press-release-skill` 的父目录中运行命令。

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills\china-daily-press-release" | Out-Null
Copy-Item -Recurse -Force ".\china-daily-press-release-skill\*" "$env:USERPROFILE\.claude\skills\china-daily-press-release"
```

### macOS

```bash
mkdir -p ~/.claude/skills
mkdir -p ~/.claude/skills/china-daily-press-release
cp -R ./china-daily-press-release-skill/. ~/.claude/skills/china-daily-press-release/
```

### Linux

```bash
mkdir -p ~/.claude/skills
mkdir -p ~/.claude/skills/china-daily-press-release
cp -R ./china-daily-press-release-skill/. ~/.claude/skills/china-daily-press-release/
```

安装后开启新的 Claude Code 会话，然后调用：

```text
$china-daily-press-release 请把以下中文材料改写成英文对外传播新闻稿。
```

如果 Claude Code 没有找到技能，请检查：

- 目录是否为 `~/.claude/skills/china-daily-press-release/`。
- `SKILL.md` 是否在该目录第一层。
- `SKILL.md` 的 YAML frontmatter 是否有效。
- 技能名是否仍为 `china-daily-press-release`。

## 目录结构

```text
china-daily-press-release-skill/
  SKILL.md
  README.md
  README.zh-CN.md
  TODO.md
  agents/
  examples/
  references/
  scripts/
  templates/
```

建议保留 `references/` 和 `templates/`。它们提供主要写作规则和输出结构。保留 `examples/` 可以让用户更快看到调用方式和输出样例。

## 输出通常包含什么

生成类任务通常会输出：

1. 英文稿或中英双语稿。
2. 事实核查清单。
3. 待确认清单。
4. 编辑说明，解释风格处理和风险处理。

审校类任务通常会输出：

1. 总体判断。
2. 阻塞性事实问题。
3. 风格问题。
4. 修改建议或修订稿。
5. 待确认清单。

## 写作边界

请尽量提供来源材料，包括活动名称、日期、地点、主办方、参与者姓名、官方职务、数据来源、已批准引语和官方英文名称。

如果某个事实缺失，技能应该标注为 `[source needed]`、`[to be confirmed]` 或 `[official English name to be confirmed]`，而不是补写。

公开 China Daily 文章只能用于风格观察。不要复制全文、长段落、独特表达或单篇文章特有结构。

## 维护说明

如果只是修改用户说明，请编辑 `README.md` 和 `README.zh-CN.md`。

如果要改变 agent 的行为，再编辑 `SKILL.md`、`references/` 或 `templates/`。

修改行为时，除非你想重命名技能，否则保留：

```yaml
name: china-daily-press-release
```
