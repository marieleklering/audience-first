# Workflow

## The Problem

One of the hardest parts of technical writing is that you already know the thing you are documenting. That makes it nearly impossible to read your own work like a newcomer would.

You have the documentation ready, but it is difficult to anticipate the context a reader will bring to it. Without early feedback, it falls to the writer to get outside their own head and produce clear documentation for readers from different backgrounds: different experience levels, different goals, different amounts of patience.

## The Solution

Use Claude to simulate specific audiences and run your content through their perspective before anyone else sees it. Not as a replacement for human review but as a structured first pass that catches the obvious gaps while they are still cheap to fix.

The key is specificity. A persona described as "a junior developer" will produce polite, generic feedback. A persona described as "a junior developer who already tried the official docs and got stuck twice" has a reason to be critical. That difference is everything.

## Why specificity matters — a quick example

Here is the same persona written two ways, and what each produces:

**Thin version:** "Sarah is a hiring manager reviewing portfolios."
Feedback it produces: "The document was clear overall. You might want to explain some technical terms."

**Friction version:** "Sarah is an engineering manager who has read eleven case studies this week. Three of them claimed impressive results with no explanation of how the numbers were measured. She is tired. She gives a document 90 seconds before deciding whether it earns more of her time. She is not trying to be fair — she is trying to triage."
Feedback it produces: "The 95% reduction figure appears twice without explaining how it was measured. If that number is wrong or loosely defined, the entire results section collapses."

Same persona and document. The friction version gives you something to actually fix.

## Why This Matters

Generic feedback is useless. "This could be clearer" tells you nothing. A persona with a specific context, a specific frustration, and a specific time budget gives you actionable signal, the kind of feedback you would get from a real reader who is not trying to be polite.

Running two personas with different experience levels surfaces two categories of problem: gaps that confuse everyone, and gaps that only appear for a specific audience. Both are worth fixing. Knowing which is which tells you where to prioritise.

**Important**: Simulated feedback has a ceiling. Claude cannot replicate genuine domain expertise, accumulated frustration with a specific product, or the instinct a practitioner develops from years of hands-on work. A persona cannot tell you that a step contradicts a common convention in a specific tool's ecosystem, or that your phrasing will land differently for a reader who has been burned by exactly this kind of problem before. Use this workflow to catch the gaps you can catch early. The gaps that remain are the ones worth taking to a human reviewer.

## The 7-Step Workflow

1. **Choose a document** — pick something mid-length, 300 to 800 words. Not so simple there is nothing to find, not so complex the feedback becomes noise. A how-to guide, a runbook section, or a case study works well.

2. **Define two personas** — write each as a short paragraph covering role, reading context, prior knowledge, and what they are suspicious of. One should be lower-experience, one higher-experience. If you want a starting point, a full persona template is available in the personas folder of this repository. The more specific the frustration and context, the more useful the feedback.

3. **Run your document through each persona using this prompt template:**
```
You are [PERSONA DESCRIPTION].

You have just read the following document for the first time.

---
[PASTE YOUR DOCUMENT HERE]
---

Answer each of the following questions from your perspective.
Be direct. Do not soften feedback. If something does not work,
say so and say why.

1. What was the main point of this document?
2. Was there anything you did not understand or had to re-read?
3. What did you expect to find that was not there?
4. Would you feel confident completing the task after reading this? Why or why not?
5. What one change would make this most useful to you?

Format your response as a numbered list matching the questions.
After the numbered responses, add a short section called
"What matters most" with one to three sentences on the single
most important thing to fix.
```

4. **Capture the output** — copy the feedback for both personas into a separate document. Tag each item as flagged by one persona or both. Items flagged by both are your highest priority fixes.

5. **Revise the document** — make the changes you decide are worth it. The personas are inputs, not editors. You decide what applies and what does not serve the purpose of the document.

6. **Re-run the same personas on the revised version** — this is the verification step. Check whether the gaps they flagged actually closed. If a persona still cannot answer question 4 confidently, you have not fixed the right thing yet.

7. **Note what you learned about your writing** — write two or three sentences about the pattern, not the document. Did both personas struggle with the same section? Did you assume prior knowledge the reader did not have? Then send for human review. The most obvious gaps are gone. Less back-and-forth will be required.
