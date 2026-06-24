# TakeMeter - planning.md
--- 
## Community 

**What community was chosen?**

The reddit community of r/unpopularopinion on the contrary is a popular community! With two point two million weekly visitors and seventy seven thousands weekly contributors the community has diverse opinions on subjects. 

**Why is this community a good fit for a classification task — what makes the discourse varied enough to be interesting?**
The community of unpopular opinion is a great fit for classification task due to its many categories and polarized opinions in those categories. 
---

## Labels

**What are your 2–4 labels? Define each in a complete sentence. Include 2 example posts per label.** 
### People 
 This label represents opinions about humans or human behavior. \
Example post: 
1. "We need to stop idolizing celebrities and start appreciating regular people. "
2. "I’ll be honest, I don’t respect janitors "

Considered an uncertain case:
- " I'd say this is a mainstream opinion these days. Unless you are dropping something at the door and don't intend to come in. But otherwise, a text is now common courtesy. "

### Objects 
 This label evaluates a concrete, consumable, or experienceable thing. 
1. "Vanilla doesn't belong in the bathroom."
2. "The steam machine isn't necessarily "too expensive". "

Considered an uncertain case: 
- "If locally-owned grocery stores want your money, they need to provide comparable prices to the corporations"

### Systems 
This labels defines posted opinions about organized structures in society that often include institutions, rules, systems, social structures. 
Example post:
1. "No child left behind started like 20+ years ago it’s not new unless I’m missing something. But also it’s been wildly unpopular ever since its inception. "
2. "The popular advice to "never admit fault" in a car accident is sociopathic and ridiculous, of course you should admit fault if you are at fault " 

Considered an uncertain case:
- "I don't think we should waste the extra tax money or teachers time on 3 more years of school for someone who isn't interested in learning"

### Ideas 
The opinion directly evaluates an abstract belief, value, or claim about truth. 
1. "Unconditional love is the biggest lie "
2. "Exercise should be prescribed with the same seriousness as medication. " 

Considered an uncertain case:
- "Modern suburbia is one of the most socially isolating environments humans have built at scale."
---

## Hard edge cases

**What type of post will be genuinely ambiguous between two labels?**
 
 A post will be considered genuinely ambiguous between two labels if the post's subject is equally two different target labels. A post in regards to System could also target and imply the label Ideas.

**How will edge cases be handled when encountered?**

Edges cases for post ambiguity will be handled by utilizing a decision rule. For example if a post reads "Social media is making people stupid", check to see what is being judged. The effect in this case is on people. The People label would be used from this decision rule. 

--- 

## Data collection plan
**Where will examples be collected from**

The data for classification will be collected from Reddit's subreddit r/unpopularopinion post as well as comments.

**How many per label?**

The classification task will be provided 50 example posts per label to aim for a total of 200 examples. 

**How will labels underrepresentations after 200 examples be handled?**

Labels with underrepresentations will be reconsidered and the labels will be revisited for weak taxonomy. Will need to check for overlapping and confusing labels or if the label is useful at all and collect more examples from the underrepresented labels. 

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

**Deployed interface:**
<!-- Build a simple interface that accepts a new post, runs it through the classifier, and displays the label and confidence. Commit the interface code to your repo and document how to run it in your README.md -->
---


## AI Tool Plan

**Label stress-testing:** 

<!-- Give the AI your label definitions and edge case description, and ask it to generate 5–10 posts that sit at the boundary between two labels. If it produces posts you can't classify cleanly, your definitions need tightening — do that now, before you annotate 200 examples. -->

**Annotation assistance:** 
 <!--Decide whether you'll use an LLM to pre-label a batch of examples before reviewing them yourself. If yes, note which tool you'll use and how you'll track which examples were pre-labeled (for disclosure in your AI usage section).-->
Will review labels for examples without the aid of an annotation assistance. 

 **Failure analysis:**
 <!--Plan to give your list of wrong predictions to an AI tool and ask it to identify patterns before you write up your evaluation. Note what you'll look for and how you'll verify the patterns yourself. --> 
Will look for repeated and over used labels 

---

 ## Spec Reflection
  <!-- Includes a substantive spec reflection with one alignment and one divergence. --> 

  **Describe one way the spec helped guide your implementation.**
  
  
  **Describe one way your implementation diverged from it and why.**