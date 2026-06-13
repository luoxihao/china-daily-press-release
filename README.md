# China Daily press release skill

Language: English | [中文](README.zh-CN.md)

This is a user guide for the `china-daily-press-release` skill. The skill helps Codex and Claude Code draft, rewrite, polish, review, and fact-check English external communication copy with China Daily-inspired style tendencies.

It is not an official China Daily tool. It must not claim China Daily publication, approval, review, authorization, or endorsement. Public China Daily articles are used only as style research sources; the skill does not store or reuse full article text.

## What it is for

Use this skill when you need to:

- Draft an English press release from verified Chinese or English source material.
- Rewrite Chinese publicity material into English news copy instead of direct translation.
- Produce bilingual Chinese-English drafts and check that the facts match.
- Polish an existing English draft so it reads more like a restrained news release.
- Review factual gaps, unsupported claims, promotional wording, Chinese-influenced English, and AI-like prose.
- Generate headline options, lead options, fact-check notes, editor notes, or a pending-confirmation list.

It works well for:

- Local government or institutional announcements.
- Cultural tourism events, city promotion, forums, exhibitions, and festivals.
- Sports events, marathons, exchange programs, and cultural heritage stories.
- Existing English drafts that need style review and fact checking.

Do not use it to:

- Imitate, rewrite, or closely follow one specific China Daily article.
- Invent facts, quotes, titles, institutions, awards, schedules, data, or official names.
- Produce advertising copy, slogans, brochure text, or unverifiable image-building claims.
- Suggest that China Daily wrote, reviewed, approved, endorsed, or published the draft.

## Quick use

In Codex or Claude Code, call the skill by name:

```text
$china-daily-press-release Please write an English external communication news draft from the following verified Chinese source material. Include a fact-check list and pending-confirmation items.
```

Review an existing draft:

```text
$china-daily-press-release Please review the following English draft for factual risk, unsupported claims, promotional tone, Chinese-influenced English, AI-like wording, and suitability for international readers.
```

Create a bilingual draft:

```text
$china-daily-press-release Please rewrite the following Chinese material into an English news draft, then provide a Chinese version and check whether the facts match across both versions.
```

If the source material is incomplete, the skill should return fact gaps and a safe draft outline instead of filling in missing facts.

## How it works

The main agent-facing file is `SKILL.md`. Its frontmatter defines the skill name and trigger description:

```yaml
name: china-daily-press-release
description: Use this skill when the user asks to write, translate, edit, polish, fact-check, localize, or review English press releases...
```

Keep `name: china-daily-press-release` unchanged if you want the `$china-daily-press-release` command to keep working. `README.md` and `README.zh-CN.md` are user documentation only; they do not control the skill name.

The skill is organized like this:

- `SKILL.md`: the agent-facing instructions, including when to use the skill, fact-first workflow, copyright boundaries, output structure, and quality checks.
- `references/`: writing rules, fact-check protocol, style checklist, phrase rules, public article style notes, and docx-derived rule summaries.
- `templates/`: output structures for English releases, bilingual releases, tourism events, sports events, cultural heritage stories, fact-check reports, and editor notes.
- `examples/`: sample invocations, sample output structure, and sample review notes.
- `scripts/`: helper scripts for rule extraction, corpus analysis, and mechanical checks.
- `agents/`: agent configuration files.

The working flow is:

1. Identify the task type: drafting, rewriting, polishing, review, fact-checking, headline options, lead options, or editor notes.
2. Extract a fact list from the source material: event name, time, place, organizers, people, numbers, quotes, background, and uncertain items.
3. Classify facts as confirmed, needing source, conflicting, missing, or not safe to use.
4. Choose the closest template.
5. Draft or edit only from confirmed facts.
6. Run style review, fact checking, and bilingual consistency checks when relevant.

The design reduces three risks: invented facts, promotional tone, and output that resembles one specific public article too closely.

## Install on Codex

Codex personal skills usually live in:

```text
~/.agents/skills/
```

Run the command from the parent directory that contains `china-daily-press-release`.

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\china-daily-press-release" "$env:USERPROFILE\.agents\skills\china-daily-press-release"
```

### macOS

```bash
mkdir -p ~/.agents/skills
cp -R ./china-daily-press-release ~/.agents/skills/china-daily-press-release
```

### Linux

```bash
mkdir -p ~/.agents/skills
cp -R ./china-daily-press-release ~/.agents/skills/china-daily-press-release
```

Start a new Codex session after installation, then call:

```text
$china-daily-press-release Please write an English news draft from this source material.
```

If Codex does not find the skill, check that:

- The folder is `~/.agents/skills/china-daily-press-release/`.
- `SKILL.md` is directly inside that folder.
- The frontmatter still contains `name: china-daily-press-release`.

## Install on Claude Code

Claude Code personal skills usually live in:

```text
~/.claude/skills/
```

Run the command from the parent directory that contains `china-daily-press-release`.

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force ".\china-daily-press-release" "$env:USERPROFILE\.claude\skills\china-daily-press-release"
```

### macOS

```bash
mkdir -p ~/.claude/skills
cp -R ./china-daily-press-release ~/.claude/skills/china-daily-press-release
```

### Linux

```bash
mkdir -p ~/.claude/skills
cp -R ./china-daily-press-release ~/.claude/skills/china-daily-press-release
```

Start a new Claude Code session after installation, then call:

```text
$china-daily-press-release Please rewrite the following Chinese source material into an English external communication news draft.
```

If Claude Code does not find the skill, check that:

- The folder is `~/.claude/skills/china-daily-press-release/`.
- `SKILL.md` is directly inside that folder.
- The frontmatter is valid YAML.
- The skill name is still `china-daily-press-release`.

## Directory layout

```text
china-daily-press-release/
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

Keep `references/` and `templates/` with the skill. They provide most of the writing guidance and output structure. Keep `examples/` if you want quick prompts and sample outputs.

## Expected output

For drafting tasks, the skill usually returns:

1. English draft or bilingual draft.
2. Fact-check list.
3. Pending-confirmation list.
4. Editor notes explaining style and risk handling.

For review tasks, the skill usually returns:

1. Verdict.
2. Blocking factual issues.
3. Style issues.
4. Suggested edits or revised draft.
5. Pending-confirmation list.

## Writing boundaries

Provide source material whenever possible: event name, date, place, organizers, participant names, official titles, data sources, approved quotes, and official English names.

If a fact is missing, the skill should mark it as `[source needed]`, `[to be confirmed]`, or `[official English name to be confirmed]`. It should not invent a missing fact.

Public China Daily articles may be used only for style observation. Do not copy full text, long passages, distinctive phrasing, or article-specific structure.

## Maintenance

Edit `README.md` and `README.zh-CN.md` for user-facing documentation.

Edit `SKILL.md`, `references/`, or `templates/` only when changing the agent's behavior.

When changing behavior, keep this frontmatter value unless you intentionally want to rename the skill:

```yaml
name: china-daily-press-release
```
