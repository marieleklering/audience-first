# Personas

This folder contains persona files used to simulate audience feedback on written
content. Each persona is a JSON file that describes a specific reader -- their
role, context, prior knowledge, and what makes them sceptical.

---

## Using an Existing Persona

Open Claude.ai and follow the prompt template in
[docs/workflow.md](../docs/workflow.md).

The included personas are:

- `hiring-manager.json` -- tired engineering manager, best for portfolio and case studies
- `senior-engineer.json` -- experienced DevOps engineer, best for technical docs and runbooks
- `ai-skeptic.json` -- senior content strategist who has abandoned three AI tools, best for docs making claims about AI workflows

---

## Building a Custom Persona

Copy `template.json` and fill in the fields:
```
cp personas/template.json personas/my-persona.json
```

Then edit `my-persona.json` covering:
- Role and industry
- Reading context (why are they reading this right now)
- Prior knowledge (what they know and what they definitely do not)
- What they are suspicious of (what would make them distrust the content)
- Time budget (reading carefully or skimming)

The more specific the frustration and context, the more useful the feedback.
A persona without a specific reason to distrust the content will default to
being polite -- and polite feedback is not useful.

---

## The Fixed Layer

Every persona includes a `fixed_layer` field that instructs the model not to
be helpful or constructive. Do not edit this field. It is what gives the
persona a critical perspective instead of a polite one.

---

For the full guide on building effective personas, see
[docs/building-personas.md](../docs/building-personas.md).
