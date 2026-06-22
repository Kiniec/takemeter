# TakeMeter - planning.md
--- 
## Community 

**What community was chosen?**


**Why is this community a good fit for a classification task — what makes the discourse varied enough to be interesting?**

---

## Labels

**What are your 2–4 labels? Define each in a complete sentence. Include 2 example posts per label.**

---

## Hard edge cases

**What type of post will be genuinely ambiguous between two labels?**

**How will edge cases be handled when encountered?**


--- 

## Data collection plan
**Where will examples be collected from**

**How many per label?**

**How will labels underrepresentations after 200 examples be handled?**

---

## Evaluation metrics

<!-- Accuracy alone is not enough - explain what else you need to and why -->
**What metrics will be used to evaluate the model and why are those the right ones for this specific task?**

---

## Definition of success
**What performance would make this classifier genuinely useful?**

**What would you accept as "good enough" for deployment in a real community tool?**


---

**Inter-annotator reliability:**
<!-- Have at least one other person label 30+ of your examples independently, and report your agreement rate (Cohen's kappa or simple percentage agreement). Analyze where you disagreed. -->

---
**Confidence calibration:** 
<!--Report whether your model's confidence scores are meaningful — does a 90% confident prediction actually get it right more often than a 60% confident one? -->

---

**Error pattern analysis:** 
<!--Go beyond listing individual wrong predictions — identify a systematic pattern in the errors (e.g., "the model consistently misclassifies sarcastic posts" or "it can't distinguish X from Y when the post is short"). -->
---

**Deployed interface: **
<!-- Build a simple interface that accepts a new post, runs it through the classifier, and displays the label and confidence. Commit the interface code to your repo and document how to run it in your README.md -->
---


## AI Tool Plan

**Label stress-testing:** 

<!-- Give the AI your label definitions and edge case description, and ask it to generate 5–10 posts that sit at the boundary between two labels. If it produces posts you can't classify cleanly, your definitions need tightening — do that now, before you annotate 200 examples. -->

**Annotation assistance:** 
 <!--Decide whether you'll use an LLM to pre-label a batch of examples before reviewing them yourself. If yes, note which tool you'll use and how you'll track which examples were pre-labeled (for disclosure in your AI usage section).-->

 **Failure analysis:**
 <!--Plan to give your list of wrong predictions to an AI tool and ask it to identify patterns before you write up your evaluation. Note what you'll look for and how you'll verify the patterns yourself. --> 

---

 ## Spec Reflection
  <!-- Includes a substantive spec reflection with one alignment and one divergence. --> 

  **Describe one way the spec helped guide your implementation.**
  
  
  **Describe one way your implementation diverged from it and why.**