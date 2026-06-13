#!/usr/bin/env python3
"""Summarize structured China Daily corpus notes into actionable style rules."""

from __future__ import annotations

import argparse
import collections
import re
from pathlib import Path


FIELDS = [
    "Headline pattern",
    "Lead pattern",
    "Paragraph structure",
    "Quote usage",
    "Attribution pattern",
    "Background information placement",
    "Cultural explanation strategy",
    "International audience adaptation",
    "Tone and diction observations",
]


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def extract_field_values(text: str, field: str) -> list[str]:
    pattern = re.compile(rf"^- {re.escape(field)}:\s*(.+)$", flags=re.M)
    values = []
    for match in pattern.finditer(text):
        value = match.group(1).strip()
        if value and not value.startswith("["):
            values.append(value)
    return values


def summarize(values: list[str], limit: int = 8) -> list[tuple[str, int]]:
    normalized = [re.sub(r"\s+", " ", v).strip().lower() for v in values if v.strip()]
    return collections.Counter(normalized).most_common(limit)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default=str(skill_root() / "references" / "china_daily_corpus_notes.md"),
        help="Corpus notes Markdown file.",
    )
    parser.add_argument(
        "--output",
        default=str(skill_root() / "references" / "china_daily_style_analysis.md"),
        help="Analysis Markdown output file.",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    text = input_path.read_text(encoding="utf-8")
    article_count = len(re.findall(r"^### \d+\.", text, flags=re.M))

    lines = [
        "# China Daily Public Corpus Style Analysis",
        "",
        f"Generated from `{input_path}`.",
        "",
        f"Structured records analyzed: {article_count}",
        "",
        "## Pattern Counts",
        "",
    ]

    for field in FIELDS:
        values = extract_field_values(text, field)
        lines.append(f"### {field}")
        if not values:
            lines.append("- No structured values found.")
        else:
            for value, count in summarize(values):
                lines.append(f"- {value} ({count})")
        lines.append("")

    lines.extend(
        [
            "## Actionable Rules",
            "",
            "- Lead with concrete event facts before background or meaning.",
            "- Use short paragraphs with one job each.",
            "- Place cultural or historical explanations after readers understand what happened.",
            "- Use quotes only after factual setup and only from verified materials.",
            "- For sports-tourism stories, connect route, participants, scenery, and public experience.",
            "- For city-promotion stories, support development claims with programs, data, or named actions.",
            "- Keep tone positive but restrained; replace vague promotional language with concrete facts.",
            "- Never copy article text or imitate a single article's sequence.",
            "",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

