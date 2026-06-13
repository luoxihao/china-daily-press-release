---
name: china-daily-press-release
description: Use this skill when the user asks to write, translate, edit, polish, fact-check, localize, or review English press releases, China Daily-style external communication articles, bilingual news drafts, cultural tourism reports, sports event releases, city promotion news, official event announcements, or Chinese-to-English news adaptations for international audiences.
---

# China Daily Press Release

## What This Skill Does

Use this skill to produce or review English external-communication news drafts with a China Daily-inspired style tendency. The skill combines local docx-derived newsroom rules, public China Daily article style observations, fact-checking discipline, bilingual consistency checks, and anti-promotional editing.

This skill does not create official China Daily copy. Use phrases such as "China Daily-style", "China Daily-inspired", or "style tendencies observed from public China Daily articles".

## When To Use This Skill

- Write an English press release or news dispatch from verified event materials.
- Rewrite Chinese source materials into English news logic rather than literal translation.
- Produce bilingual Chinese-English drafts with aligned facts.
- Polish an English draft toward restrained, fact-first external communication.
- Review a draft for Chinese-English interference, promotional tone, AI-generic wording, unsupported claims, fabricated quotes, or missing sources.
- Generate a fact-check report, editor notes, title options, lead options, or a pending-confirmation list.

## When Not To Use This Skill

- Do not use it to imitate, reproduce, or closely paraphrase any specific China Daily article.
- Do not use it to claim publication, approval, authorization, review, or endorsement by China Daily.
- Do not use it when the user wants advertising copy, slogans, tourism brochure language, or unverifiable image-building claims.
- Do not invent facts, quotes, people, institutions, dates, data, outcomes, awards, schedules, or organizer names to make a draft feel complete.

## Required References To Consult

Before drafting or reviewing, read or cite the relevant files directly:

- `references/merged_writing_rules.md`
- `references/fact_check_protocol.md`
- `references/style_checklist.md`
- `references/phrase_rules.md`
- `references/china_daily_style_analysis.md`
- `references/docx_rule_summary.md` when source materials conflict with docx-derived guidance

Use `templates/` for output structure and `scripts/validate_press_release.py` for mechanical checks.

## China Daily Corpus Analysis Rules

- Treat public China Daily articles as style research sources, not reusable text.
- Store only URL, title, date, topic, structure notes, and style observations.
- Do not store article full text or long excerpts.
- Extract transferable patterns: headline economy, fact-first lead, short paragraphs, attribution habits, background placement, restrained positive diction, and international-reader explanations.
- When a corpus observation conflicts with verified user materials, preserve the verified facts and adapt only style or structure.

## Docx-Derived Rules

- Find the news point before writing; do not treat the event name as the lead by default.
- Build a fact list first, then select the angle.
- Use short paragraphs with a function: fact, quote, background, explanation, or transition.
- Avoid slogans, broad significance claims, and unverifiable praise.
- Use direct quotes only from provided or source-approved materials.
- Put uncertain translations, titles, proper nouns, and numbers on a pending-confirmation list.
- Convert Chinese units and money for international readers when appropriate.

## Fact-First Workflow

1. Identify the task type: generation, Chinese-to-English rewrite, bilingual draft, polish, review, fact-check, headline/lead, editor notes, or style adaptation.
2. Extract a fact list before writing: event name, time, place, organizers, co-organizers, participants, countries/regions, guests, quotes, background, cultural context, sports categories, data sources, and pending items.
3. Classify facts as `Confirmed`, `Likely but needs source`, `Conflicting`, `Missing`, or `Should not be used`.
4. Choose the closest template: English press release, bilingual release, tourism event, sports event, or cultural heritage.
5. Draft only from confirmed facts. Mark uncertain facts as `[to be confirmed]`.
6. Run a style review and fact check before final output.

## English Press Release Workflow

- Use a concise news headline, not a promotional slogan.
- Start with who/what/when/where/why/how or the strongest verified outcome.
- Keep the lead to one or two sentences.
- Put event facts before background, policy meaning, or tourism/cultural significance.
- Explain Chinese places, heritage, customs, or institutions for international readers.
- Use positive but restrained wording.
- Remove tourist-advertising tone, Chinese policy-slogan translation, and AI-generic phrasing.
- Do not use unsupported superlatives.

## Chinese Version Workflow

- Preserve the same fact base as the English draft.
- Write natural Chinese news prose rather than back-translating English sentence by sentence.
- Do not add facts absent from the English draft or source materials.
- Keep English names, titles, institutions, and uncertain translations annotated when needed.
- Preserve pending-confirmation markers in the Chinese version as an explicit pending-confirmation note.

## Bilingual Consistency Workflow

- Compare event name, date, place, organizers, participant numbers, quotes, data, and proper nouns across both versions.
- Resolve inconsistency by returning to the source materials, not by guessing.
- Keep quote meaning aligned; never create a quote in one language that does not exist in the other source.
- Output a bilingual consistency note when material facts remain uncertain.

## Style Review Workflow

Review for:

- Lead answers the central news question.
- Paragraphs are short and purposeful.
- Background arrives after the event facts.
- Claims have sources or pending-confirmation markers.
- Quotes are attributed and supplied by source materials.
- Tone is objective-positive, not exaggerated.
- Chinese officialese, slogan translation, and tourist-advertising language are reduced.
- International readers get enough context without a lecture.
- The draft does not resemble any specific public article.

## Anti-Fabrication Rules

- Never fabricate direct quotes, paraphrased statements, people, affiliations, institutions, data, rankings, event schedules, awards, or official positions.
- If a quote is desirable but not provided, write: `[approved quote needed]`.
- If a number lacks a source, write: `[source needed]`.
- If an official English name is uncertain, write: `[official English name to be confirmed]`.
- If source materials conflict, list the conflict and ask for confirmation before using the claim.

## Copyright And Non-Imitation Policy

- Use public China Daily articles only to observe transferable style tendencies.
- Do not copy full text, long passages, distinctive sequencing, or article-specific phrasing.
- Do not produce a draft that is substantially similar to any individual article.
- Do not imply China Daily wrote, approved, authorized, endorsed, or will publish the draft.

## Output Structure

For generation tasks, output:

1. English draft or requested bilingual draft
2. Fact-check list
3. Pending-confirmation list
4. Editor notes explaining style choices and risk handling

For review tasks, output:

1. Verdict
2. Blocking factual issues
3. Style issues
4. Suggested edits or revised version
5. Pending-confirmation list

## Quality Checklist

- [ ] Fact list completed before drafting
- [ ] No invented facts or quotes
- [ ] Title is concise and news-like
- [ ] Lead contains the strongest verified news point
- [ ] Paragraphs are short
- [ ] Background follows key facts
- [ ] Data and dates have sources or confirmation markers
- [ ] Cultural context is clear for international readers
- [ ] Tone is positive but restrained
- [ ] Chinese-English interference reduced
- [ ] AI-generic wording removed
- [ ] Bilingual facts align when applicable
- [ ] No claim of official China Daily status

## Failure Handling

- If source facts are insufficient, produce a fact-gap report and a safe skeleton draft rather than inventing details.
- If no docx rules are available, use `references/web_research_plan.md` and mark docx-derived rules as pending.
- If web research is unavailable, do not pretend corpus research happened; record the limitation and use only available references.
- If a user asks for unsupported claims, refuse the unsupported portion and offer a sourced or pending-confirmation alternative.

## Example Invocations

See `examples/sample_invocations.md` for ready-to-use prompts, including Huangyaguan Great Wall Marathon, Chinese-to-English rewriting, draft polishing, fact-checking, and AI-tone removal.
