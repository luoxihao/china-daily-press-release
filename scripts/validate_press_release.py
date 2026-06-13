#!/usr/bin/env python3
"""Heuristic validator for English external-communication news drafts."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


PROMOTIONAL = [
    "successfully held",
    "grandly held",
    "inject vitality",
    "new vitality",
    "fully demonstrates",
    "fruitful results",
    "world-class",
    "unprecedented",
    "unique charm",
    "beautiful name card",
]

CHINESE_ENGLISH = [
    "under the background of",
    "in order to further",
    "relevant departments",
    "the masses",
    "all walks of life",
    "rich and colorful",
    "was warmly welcomed by",
]

AI_GENERIC = [
    "serves as a bridge",
    "plays an important role",
    "marks a significant step",
    "has attracted widespread attention",
    "will further promote",
    "opened a new chapter",
]

SUPERLATIVES = [
    "first",
    "largest",
    "best",
    "most",
    "leading",
    "world-class",
    "unprecedented",
]

CHINESE_PUNCTUATION = "，。；：“”‘’（）【】《》、"


@dataclass
class Finding:
    severity: str
    check: str
    message: str


def nonempty_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def paragraphs(text: str) -> list[str]:
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    return [b for b in blocks if not b.startswith("#") and not b.startswith("|")]


def contains_attribution(paragraph: str) -> bool:
    return bool(
        re.search(
            r"\b(said|according to|the organizer|the bureau|the authority|the report|data from|officials)\b",
            paragraph,
            flags=re.I,
        )
    )


def validate(text: str) -> list[Finding]:
    findings: list[Finding] = []
    lines = nonempty_lines(text)
    body_paragraphs = paragraphs(text)

    if not lines:
        return [Finding("error", "empty", "The file is empty.")]

    has_title = lines[0].startswith("#") or len(lines[0].split()) <= 16
    if not has_title:
        findings.append(Finding("error", "title", "No clear title or headline found at the top."))

    lead_candidates = [p for p in body_paragraphs if len(p.split()) >= 12]
    if not lead_candidates:
        findings.append(Finding("error", "lead", "No lead paragraph found."))
    else:
        lead = lead_candidates[0]
        if len(lead.split()) > 80:
            findings.append(Finding("warning", "lead", "Lead paragraph is long; aim for one or two concise sentences."))
        if not re.search(r"\b(on|in|at|from|during|held|opened|launched|joined|drew|featured)\b", lead, re.I):
            findings.append(Finding("warning", "lead", "Lead may not answer core news facts clearly."))

    for idx, para in enumerate(body_paragraphs, 1):
        words = para.split()
        if len(words) > 95:
            findings.append(Finding("warning", "paragraph length", f"Paragraph {idx} has {len(words)} words."))

    lowered = text.lower()
    for phrase in PROMOTIONAL:
        if phrase in lowered:
            findings.append(Finding("warning", "promotional tone", f"Promotional phrase detected: `{phrase}`."))

    for phrase in CHINESE_ENGLISH:
        if phrase in lowered:
            findings.append(Finding("warning", "Chinese-English risk", f"Possible Chinese-English expression: `{phrase}`."))

    for phrase in AI_GENERIC:
        if phrase in lowered:
            findings.append(Finding("warning", "AI-generic wording", f"Generic phrase detected: `{phrase}`."))

    for mark in CHINESE_PUNCTUATION:
        if mark in text:
            findings.append(Finding("warning", "punctuation", f"Chinese punctuation detected: `{mark}`."))
            break

    number_pattern = r"(?<!\w)(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:\s?(percent|km|kilometers|people|participants|countries|regions|yuan|dollars|million|billion))?"
    for match in re.finditer(number_pattern, text, re.I):
        start = max(0, match.start() - 120)
        end = min(len(text), match.end() + 120)
        context = text[start:end]
        if not re.search(r"according to|data from|source|said|reported|showed|\[source needed\]", context, re.I):
            findings.append(Finding("warning", "number source", f"Number may need source: `{match.group(0)}`."))

    for quote_match in re.finditer(r"([\"“][^\"”]{30,}[.!?,;:][^\"”]*[\"”])", text):
        start = max(0, quote_match.start() - 120)
        end = min(len(text), quote_match.end() + 160)
        context = text[start:end]
        if not contains_attribution(context):
            findings.append(Finding("error", "quote attribution", "Direct quote may lack clear attribution."))

    for word in SUPERLATIVES:
        for match in re.finditer(rf"\b{re.escape(word)}\b", text, flags=re.I):
            start = max(0, match.start() - 100)
            end = min(len(text), match.end() + 100)
            context = text[start:end]
            if not re.search(r"according to|ranked|source|record|official|one of|\[source needed\]", context, re.I):
                findings.append(Finding("warning", "unsupported superlative", f"Check support for `{word}`."))
                break

    if "[to be confirmed]" in lowered or "[source needed]" in lowered:
        findings.append(Finding("info", "pending information", "Draft contains pending-confirmation markers."))

    if len(body_paragraphs) < 4:
        findings.append(Finding("warning", "structure", "Draft may be structurally thin; check facts, background, and source notes."))

    return findings


def render(findings: list[Finding]) -> str:
    if not findings:
        return "# Validation Report\n\nNo heuristic issues found.\n"

    lines = ["# Validation Report", ""]
    for severity in ["error", "warning", "info"]:
        group = [f for f in findings if f.severity == severity]
        if not group:
            continue
        lines.append(f"## {severity.title()}s")
        lines.append("")
        for item in group:
            lines.append(f"- **{item.check}**: {item.message}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", help="Markdown draft to validate.")
    parser.add_argument("--output", help="Optional Markdown report path.")
    parser.add_argument("--strict", action="store_true", help="Exit 1 when errors or warnings are found.")
    args = parser.parse_args()

    draft = Path(args.draft)
    text = draft.read_text(encoding="utf-8")
    report = render(validate(text))
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    print(report, end="")

    if args.strict and re.search(r"^## (Errors|Warnings)", report, flags=re.M):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
