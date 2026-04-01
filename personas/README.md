# Personas

This folder contains persona files used to simulate audience feedback on written content.
Each persona is a JSON file that describes a specific reader — their role, context,
prior knowledge, and what makes them sceptical.

## Using an existing persona

```bash
python run.py --doc yourfile.md --persona personas/hiring-manager.json
python run.py --doc yourfile.md --persona personas/senior-engineer.json --mode friction
```

## Building a custom persona

Copy `template.json` and fill in the fields:

```bash
cp personas/template.json personas/my-persona.json
```

Then edit `my-persona.json` with a specific role, reading context, and what the
persona is suspicious of. The more specific the context, the more useful the feedback.

## The Fixed Layer

Every persona includes a `fixed_layer` field that instructs the model not to be
helpful or constructive. Do not edit this field. It is what gives the persona a
critical perspective instead of a polite one — and polite feedback is not useful.

For the full guide on building effective personas, see `docs/building-personas.md`.
