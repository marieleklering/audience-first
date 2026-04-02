# AudienceFirst
Simulate audience feedback on your docs before anyone else reads them.

---

## Two ways to use this

**Option 1 — CLI tool:** Run feedback directly from your terminal using the
Python script and the Anthropic API. Faster and repeatable once set up.

**Option 2 — Manual workflow:** Run the same methodology directly in
Claude.ai with no setup, no API key, and no cost. Paste your document,
paste your persona, paste the questions, get feedback.

→ If you want to get started immediately with no setup: read [docs/workflow.md](docs/workflow.md)
→ If you want a repeatable CLI tool: follow the Quick Start below

---

## Quick Start (CLI)
```bash
git clone https://github.com/YOUR_USERNAME/audience-first.git
cd audience-first
pip install -r requirements.txt
cp .env.example .env        # then add your Anthropic API key
python run.py --doc your-document.md --persona personas/hiring-manager.json
```

---

## Usage Examples
```bash
# Default — general technical documentation
python run.py --doc guide.md --persona personas/hiring-manager.json

# Friction — when default feedback feels too comfortable
python run.py --doc guide.md --persona personas/senior-engineer.json --mode friction

# Portfolio — for case studies and portfolio pieces
python run.py --doc case-study.md --persona personas/hiring-manager.json --mode portfolio
```

---

## How It Works

AudienceFirst loads a persona JSON file and a document, builds a prompt
that puts Claude in the persona's perspective, and asks a structured set
of questions about the content. The persona's role, reading context, prior
knowledge, and suspicions shape the feedback — making it specific to a real
reader type rather than a generic review.

See [docs/workflow.md](docs/workflow.md) for the full methodology, including
how to build effective personas, when to use friction questions, and how to
act on the feedback you get.

---

## Included Personas

| File | Who they are | Best for |
|---|---|---|
| `hiring-manager.json` | Tired engineering manager, 90-second attention budget | Portfolio, case studies |
| `senior-engineer.json` | Experienced DevOps, skims to technical detail | Technical docs, runbooks |

See [personas/README.md](personas/README.md) for instructions on building your own.

---

## Question Modes

| Mode | Best for |
|---|---|
| `default` | Technical docs, how-to guides, runbooks |
| `friction` | When default feedback feels too polite |
| `portfolio` | Case studies, portfolio pieces |

See [docs/question-sets.md](docs/question-sets.md) for the full question sets.

---

## Requirements

For the CLI tool:
- Python 3.8 or higher
- Anthropic API key — get one at [console.anthropic.com](https://console.anthropic.com)

For the manual workflow:
- A Claude.ai account (free tier is enough)

---

## Contributing

Contributions are welcome. Persona contributions are especially valuable —
if you build a useful persona for a content type not covered by the included
examples, open a PR and add it to the `personas/` folder with a clear name
and realistic field values.

---

## License

MIT
