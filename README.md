# AudienceFirst
Stop sending documentation for review before you have caught the obvious gaps yourself.

AudienceFirst uses Claude to simulate how specific readers will respond to your
content before anyone else sees it. Not as a replacement for human review, but
as a structured first pass that catches the gaps while they are still cheap to fix.

No setup required. Run it right now in Claude.ai with no API key and no cost.

---

## How to Use This

Read [docs/workflow.md](docs/workflow.md) for the full 7-step methodology.

The short version:
1. Define two personas representing different readers of your content
2. Paste your document and persona into Claude.ai using the prompt template
   in [docs/workflow.md](docs/workflow.md)
3. Capture the feedback, revise, and re-run to verify the gaps closed

A full cycle takes around 15 minutes, not counting the time to apply feedback.

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

## What Is Coming

A Python CLI that runs the workflow from your terminal using the Anthropic API.
Faster and repeatable once set up. In development for a future version.

---

## Contributing

Contributions are welcome. Persona contributions are especially valuable -- if
you build a useful persona for a content type not covered by the included
examples, open a PR and add it to the `personas/` folder with a clear name
and realistic field values.

---

## License

MIT
