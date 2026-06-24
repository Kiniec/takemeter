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
- Decision:  labeled people - this is an opinion about behavior in which a person by do by arriving at a another person's house unannounced.

### Objects 
 This label evaluates a concrete, consumable, or experienceable thing. 
1. "Vanilla doesn't belong in the bathroom."
2. "The steam machine isn't necessarily "too expensive". "

Considered an uncertain case: 
- "If locally-owned grocery stores want your money, they need to provide comparable prices to the corporations"
-  Decision: labeled systems — this is an opinion about market structure and corporate competition, not the grocery store as a physical/consumable thing.

### Systems 
This labels defines posted opinions about organized structures in society that often include institutions, rules, systems, social structures. 
Example post:
1. "No child left behind started like 20+ years ago it’s not new unless I’m missing something. But also it’s been wildly unpopular ever since its inception. "
2. "The popular advice to "never admit fault" in a car accident is sociopathic and ridiculous, of course you should admit fault if you are at fault " 

Considered an uncertain case:
- "I don't think we should waste the extra tax money or teachers time on 3 more years of school for someone who isn't interested in learning" 
-  Decision: labeled systems - the post is an opinion that points out a government rule and something pertaining to an institution - "tax money", "teachers".

### Ideas 
The opinion directly evaluates an abstract belief, value, or claim about truth. 
1. "Unconditional love is the biggest lie "
2. "Exercise should be prescribed with the same seriousness as medication. " 

Considered an uncertain case:
- "Modern suburbia is one of the most socially isolating environments humans have built at scale."
-  Decision: labeled ideas — this is an opinion about socially induced environments for humans.


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
 Accuracy alone isn't sufficient because the dataset may be imbalanced across labels. F1-score per class will be used so that weak performance on a minority label (e.g., Systems) isn't hidden by strong performance on Objects. Macro-averaged F1 gives equal weight to each label regardless of size.

---

## Definition of success
**What performance would make this classifier genuinely useful?**
 A macro F1 of 0.65 or above across all four labels would be considered "good enough" for deployment. A classifier that performs at or below majority-class baseline (predicting "Objects" every time) would not be acceptable regardless of accuracy.


**What would you accept as "good enough" for deployment in a real community tool?**
A macro F1 of 0.65 with no individual class below 0.50 would be acceptable for deployment. Systems is the most critical class — a classifier that can't distinguish institutional critique from object-level opinions would be misleading to community moderators.


---

**Inter-annotator reliability:**
<!-- Have at least one other person label 30+ of your examples independently, and report your agreement rate (Cohen's kappa or simple percentage agreement). Analyze where you disagreed. -->
Utilizing an outside source to label examples independently, the agreement rate on averages was only 30%. The most disagreeable labels were "objects" with "people" coming in second. The label "objects" seems to be the most polarized due its broad covering topics and subject. 

---
**Confidence calibration:** 
<!--Report whether your model's confidence scores are meaningful — does a 90% confident prediction actually get it right more often than a 60% confident one? -->

 The model's confidence scores showed limited correlation with accuracy. Predictions in the 90–100% confidence range were correct 71% of the time, while predictions in the 60–70% range were correct 50% of the time. This suggests the model is overconfident — it assigns high softmax probabilities even on categories it misclassifies (particularly Systems, which scored 0.00 F1 but still received high-confidence wrong predictions). A well-calibrated model would show accuracy ≈ confidence at each bucket; the gap here reflects that DistilBERT's softmax outputs are not reliable probability estimates without additional calibration (e.g., temperature scaling).

---

**Error pattern analysis:** 
<!--Go beyond listing individual wrong predictions — identify a systematic pattern in the errors (e.g., "the model consistently misclassifies sarcastic posts" or "it can't distinguish X from Y when the post is short"). -->

Systems scored 0.00 F1 — every single Systems post was misclassified. The pattern across all 3 wrong predictions is the same: the model classifies based on the dominant noun (school, shower, property) rather than the nature of the judgment. When a post critiques a rule or institution using a physical anchor word, the model assigns Objects or People instead of Systems.  

--- 

**Deployed interface:**
<!-- Build a simple interface that accepts a new post, runs it through the classifier, and displays the label and confidence. Commit the interface code to your repo and document how to run it in your README.md -->

---


## AI Tool Plan

**Label stress-testing:** 

<!-- Give the AI your label definitions and edge case description, and ask it to generate 5–10 posts that sit at the boundary between two labels. If it produces posts you can't classify cleanly, your definitions need tightening — do that now, before you annotate 200 examples. -->
Provided AI label definitions of people, objects, systems, and ideas along with edge case descriptions. Instructed to generate 5-10 posts that sit at the boundary between two labels. The results did not show case a clean classification. The definitions had to b tightened to remove ambiguity.  
Provided Claude Code with the list of wrong predictions from the test set. Asked it to identify patterns across misclassified examples. The AI identified the noun-anchoring pattern (classifying based on the subject word rather than the nature of the critique), which was then verified manually against the confusion matrix.


**Annotation assistance:** 
 <!--Decide whether you'll use an LLM to pre-label a batch of examples before reviewing them yourself. If yes, note which tool you'll use and how you'll track which examples were pre-labeled (for disclosure in your AI usage section).-->
Will review labels for examples without the aid of an annotation assistance. 

 **Failure analysis:**
 <!--Plan to give your list of wrong predictions to an AI tool and ask it to identify patterns before you write up your evaluation. Note what you'll look for and how you'll verify the patterns yourself. --> 
Will provide a list of wrong predictions to the AI tool and look confidence scores and will verify the pattern by reviewing the fine-tuned model set.

---
