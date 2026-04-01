# Building Personas

## The Persona Template

```
PERSONA NAME: [give them a name]
ROLE: [job title and industry]
READING CONTEXT: [why are they reading this right now]
PRIOR KNOWLEDGE: [what they already know / what they definitely do not know]
SUSPICIOUS OF: [what would make them doubt the content]
TIME BUDGET: [reading carefully or skimming]

FIXED LAYER [do not edit]:
This persona is not trying to be helpful or constructive.
They have better things to do. If the content does not earn their
attention in the first paragraph, they stop. They do not give
the benefit of the doubt.
```

## The Suspicious Of Field

The `suspicious_of` field is the most important field to fill in carefully. It
tells the persona what to watch for — and turns a generic reader into a sceptical
one with a specific lens.

### Suspicious Of Reference Table

| Content type | Common suspicions |
|---|---|
| Portfolio / case studies | Vague metrics, diluted ownership, stories that skip the low point |
| Technical documentation | Steps that skip assumed knowledge, configuration examples too clean to be real |
| Marketing / social content | Humble-brag as advice, impressive claims with no evidence |
| Internal communications | Buried ask, unclear ownership of next steps |

## Friction Parameters

To get more honest, uncomfortable feedback, add friction to the persona:

- **Prior failure** — give them a specific frustration before they start reading
- **Competing priorities** — put them under time pressure
- **Explicit suspicion** — tell them what to distrust
- **No politeness mandate** — add "You are not trying to be helpful" explicitly

## How to Know If a Persona Is Working

A persona is working when the feedback is specific enough to act on. Vague feedback
("this was unclear") means the persona lacks enough context. Specific feedback
("I stopped at the third step because you assumed I already had X configured")
means the persona has a real perspective.

If all your feedback feels polite and positive, your persona does not have enough
friction. Add prior failure or explicit suspicion and re-run.

## Worked Example: Agreeable vs Friction Version of Sarah

### Agreeable Sarah (too generic)

```json
{
  "name": "Sarah",
  "role": "Engineering manager",
  "reading_context": "Reviewing a portfolio submission",
  "prior_knowledge": "Some technical background",
  "suspicious_of": "Exaggerated claims",
  "time_budget": "Limited",
  "fixed_layer": "..."
}
```

This will produce polite, surface-level feedback. The context is too thin to generate
a real perspective.

### Friction Sarah (specific and useful)

```json
{
  "name": "Sarah",
  "role": "Engineering manager at a mid-size SaaS company",
  "reading_context": "Has spent two weeks reviewing portfolio submissions. Has already read eleven case studies. Three of them claimed significant metric improvements with no explanation of how those numbers were measured. She is tired.",
  "prior_knowledge": "Enough technical literacy to follow a high-level narrative, but does not work hands-on with infrastructure tools. Needs the story before the technical detail.",
  "suspicious_of": "Vague 'we' language that hides individual contribution. Metrics that sound precise but are not sourced. Solutions presented as cleaner in hindsight than they probably were in reality.",
  "time_budget": "Reading on a laptop between back-to-back meetings. Gives a document about 90 seconds before deciding whether it earns more of her time.",
  "fixed_layer": "This persona is not trying to be helpful or constructive. She is not trying to be fair. She is trying to triage. If the content does not earn her attention in the first paragraph, she moves on."
}
```

The second version has a specific frustration (eleven case studies, three with unsourced
metrics), a specific time constraint (90 seconds, between meetings), and a specific
suspicion (vague 'we' language). The feedback it produces will be actionable.
