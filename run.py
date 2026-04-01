#!/usr/bin/env python3
"""
AudienceFirst — Simulate audience feedback on written content before anyone else reads it.

Usage:
    python run.py --doc <path> --persona <path> [--mode <mode>]

Modes:
    default     General technical documentation (default)
    friction    When you need more honest, uncomfortable feedback
    portfolio   Portfolio pieces and case studies
    marketing   Marketing copy, newsletters, social content

Examples:
    python run.py --doc my-guide.md --persona personas/hiring-manager.json
    python run.py --doc case-study.md --persona personas/senior-engineer.json --mode friction
    python run.py --doc blog-post.md --persona personas/hiring-manager.json --mode marketing
"""

import argparse
import json
import os
import sys
from pathlib import Path

import anthropic
from dotenv import load_dotenv

load_dotenv()

# ── Question Sets ──────────────────────────────────────────────────────────────

QUESTION_SETS = {
    "default": [
        "What was the main point of this document?",
        "Was there anything you did not understand or had to re-read?",
        "What did you expect to find that was not there?",
        "Would you feel confident completing the task after reading this? Why or why not?",
        "What one change would make this most useful to you?"
    ],
    "friction": [
        "Where did you stop reading, even briefly, and why?",
        "What would you tell a colleague this document got wrong or oversimplified?",
        "What would make you trust this less?",
        "What is the one thing the author clearly does not want you to notice?",
        "Would you share this with a colleague or quietly close the tab?"
    ],
    "portfolio": [
        "What was the main point of this document?",
        "Was there anything you did not understand or had to re-read?",
        "What did you expect to find that was not there?",
        "Does the author's specific contribution come through clearly? What did they own?",
        "What one change would make this most convincing?"
    ],
    "marketing": [
        "Would you keep reading after the first two sentences? Why or why not?",
        "What do you think this person is trying to sell or prove?",
        "Does anything feel off or inauthentic?",
        "What would make you share this?",
        "What is missing that would make this more useful to you?"
    ]
}

# ── Prompt Builder ─────────────────────────────────────────────────────────────

def build_prompt(persona: dict, document_text: str, questions: list[str]) -> str:
    persona_description = f"""You are {persona['name']}.
Role: {persona['role']}
Reading context: {persona['reading_context']}
Prior knowledge: {persona['prior_knowledge']}
Suspicious of: {persona['suspicious_of']}
Time budget: {persona['time_budget']}

Important: {persona['fixed_layer']}"""

    numbered_questions = "\n".join(
        f"{i + 1}. {q}" for i, q in enumerate(questions)
    )

    return f"""{persona_description}

You have just read the following document for the first time.

---
{document_text}
---

Answer each of the following questions from your perspective as {persona['name']}.
Be direct. Do not soften feedback. If something does not work, say so and say why.

{numbered_questions}

Format your response as a numbered list matching the questions.
After the numbered responses, add a section called "What matters most"
with one to three sentences on the single most important thing to fix."""

# ── Output Formatting ──────────────────────────────────────────────────────────

def print_header(persona_name: str, doc_path: str, mode: str) -> None:
    print("\n" + "─" * 60)
    print(f"  AUDIENCE FIRST")
    print(f"  Persona : {persona_name}")
    print(f"  Document: {doc_path}")
    print(f"  Mode    : {mode}")
    print("─" * 60 + "\n")

def print_feedback(feedback: str) -> None:
    print(feedback)
    print("\n" + "─" * 60 + "\n")

def print_error(message: str) -> None:
    print(f"\n  Error: {message}\n", file=sys.stderr)

# ── API Call ───────────────────────────────────────────────────────────────────

def run_feedback(prompt: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text

# ── CLI ────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="AudienceFirst — Simulate audience feedback on written content.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--doc", required=True, help="Path to the document file (.txt or .md)")
    parser.add_argument("--persona", required=True, help="Path to a persona JSON file")
    parser.add_argument(
        "--mode",
        choices=list(QUESTION_SETS.keys()),
        default="default",
        help="Question set to use (default: default)"
    )

    args = parser.parse_args()

    # Validate inputs
    doc_path = Path(args.doc)
    persona_path = Path(args.persona)

    if not doc_path.exists():
        print_error(f"Document not found: {args.doc}")
        sys.exit(1)

    if not persona_path.exists():
        print_error(f"Persona file not found: {args.persona}")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print_error("ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key.")
        sys.exit(1)

    # Load files
    document_text = doc_path.read_text(encoding="utf-8")
    persona = json.loads(persona_path.read_text(encoding="utf-8"))
    questions = QUESTION_SETS[args.mode]

    # Run
    print_header(persona["name"], args.doc, args.mode)
    print("  Running feedback...\n")

    prompt = build_prompt(persona, document_text, questions)
    feedback = run_feedback(prompt)

    print_feedback(feedback)


if __name__ == "__main__":
    main()
