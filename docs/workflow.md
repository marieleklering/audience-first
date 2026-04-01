# Workflow

## The Problem

One of the hardest parts of technical writing is that you already know the thing
you are documenting. That makes it nearly impossible to read your own work like
a newcomer would.

You have the documentation ready, but it is difficult to anticipate the context
a reader will bring to it. Without early feedback, it falls to the writer to get
outside their own head and produce clear documentation for readers from different
backgrounds — different experience levels, different goals, different amounts of
patience.

## The Solution

Use Claude to simulate specific audiences and run your content through their
perspective before anyone else sees it. Not as a replacement for human review —
but as a structured first pass that catches the obvious gaps while they are still
cheap to fix.

The key is specificity. A persona described as "a junior developer" will produce
polite, generic feedback. A persona described as "a junior developer who already
tried the official docs and got stuck twice" has a reason to be critical.

## Why This Matters

Generic feedback is useless. "This could be clearer" tells you nothing. A persona
with a specific context, a specific frustration, and a specific time budget gives
you actionable signal — the kind of feedback you would get from a real reader who
is not trying to be polite.

Running two personas with different experience levels surfaces two categories of
problem: gaps that confuse everyone, and gaps that only appear for a specific audience.
Both are worth fixing. Knowing which is which tells you where to prioritise.

## The 7-Step Workflow

1. Choose a document (300–800 words, mid-complexity)
2. Define two personas (lower-experience and higher-experience)
3. Build your feedback prompt using the question sets
4. Run and capture output for both personas without editing between runs
5. Revise the document based on feedback you decide applies
6. Re-run the same personas on the revised version to verify gaps closed
7. Note what you learned about your writing patterns, then send for human review
