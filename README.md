# AudienceFirst v1.0
Stop sending documentation for review before you have caught the obvious gaps yourself.

AudienceFirst gives you a structured way to do that, simulating how specific readers will respond to your content before anyone else sees it. 
Not as a replacement for human review, but as a first pass that catches the gaps while they are still cheap to fix.

No setup required. Run it right now in Claude.ai with no API key and no cost.

---

## How to Use This

There are three ways to run AudienceFirst depending on your preference.

**Option 1 - Manual workflow (free, no setup)**
Run the methodology directly in Claude.ai. Paste your document, paste
your persona, paste the questions, get feedback. Everything you need
is in [workflow.md](docs/workflow.md).

**Option 2 - Claude Project (free, faster)**
Set up AudienceFirst as a Claude Project so you never have to paste
personas or questions again. Open a new Project in Claude.ai, paste
the system prompt from
[claude-project-setup.md](claude-project-setup.md), and run feedback
with a single line: "run Sarah, friction mode" from that point on.

**Option 3 - CLI tool (coming soon)**
A Python CLI that runs the workflow from your terminal using the
Anthropic API. In development for a future version.

**Both Option 1 and Option 2 work on the free tier of Claude.ai.
A full cycle takes around 15 minutes, not counting the time to apply
feedback.**

---

## Included Personas

Three personas are included as starting points. They cover the most common
reader types technical writers need to account for: a non-technical evaluator,
an experienced practitioner, and a sceptical reader who needs to be convinced
the methodology holds up before investing time in it.

| File | Who they are | Best for |
|---|---|---|
| `hiring-manager.json` | Tired engineering manager, 90-second attention budget | Portfolio, case studies |
| `senior-engineer.json` | Experienced DevOps, skims to technical detail | Technical docs, runbooks |
| `ai-skeptic.json` | Senior content strategist, has abandoned three AI tools, low expectations | Docs making claims about AI tools |

See [personas/README.md](personas/README.md) for instructions on building your own.

---

## Question Modes

Three question sets are available depending on what your document needs.

| Mode | Best for |
|---|---|
| `default` | Technical docs, how-to guides, runbooks |
| `friction` | When default feedback feels too polite |
| `portfolio` | Case studies, portfolio pieces |

See [docs/question-sets.md](docs/question-sets.md) for the full question sets
and guidance on when to use each one.

---

## Requirements

A Claude.ai account. The free tier is enough to run the workflow.

---

## Contributing

Contributions are welcome. Persona contributions are especially valuable, if
you build a useful persona for a content type not covered by the included
examples, open a PR and add it to the `personas/` folder with a clear name
and realistic field values.

---

## License

MIT
