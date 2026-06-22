# Project 3: TakeMeter

**Total Points: 25pts + 4pts bonus**

## Required Features

### Label Taxonomy (3pts)
- 2–4 labels are defined in complete sentences with clear boundaries between them.
- Each label has 2 example posts included.
- Definitions are specific enough that two people reading them would likely agree on most cases — not one-word descriptions or vague adjectives.

### Annotated Dataset (4pts)
- Dataset has at least 200 labeled examples.
- README documents the data source, labeling process, and label distribution (count per label).
- At least 3 genuinely difficult examples are described, including the labeling decision made for each.
- No single label accounts for more than 70% of the dataset.

### Fine-Tuning Pipeline (2pts)
- README names the base model and the training platform (e.g., Colab, local, HuggingFace AutoTrain).
- At least one key training decision is described and justified (e.g., number of epochs, learning rate, or batch size).

### Baseline Comparison (2pts)
- README describes the baseline approach — the prompt used and how results were collected.
- Evaluation report shows performance metrics for both the fine-tuned model and the baseline on the same test set.

### Evaluation Report and Error Analysis (5pts)
- At least one per-class metric is reported (precision, recall, or F1 — not just overall accuracy).
- A confusion matrix or equivalent table is included.
- At least 3 specific wrong predictions are analyzed with explanations.
- A reflection on the gap between what the model captured and what was intended, with a specific failure pattern.

### planning.md (4pts)
- Community choice is explained with reasoning for fit.
- Labels are defined with examples and the hardest anticipated edge case is addressed.
- Data collection plan and evaluation metrics are described with reasoning.
- A specific definition of “good enough” performance is given.
- AI Tool Plan includes at least one intended use.

### Demo Video (3pts)
- Shows 3–5 posts classified with label and confidence.
- Includes one correct prediction explanation.
- Includes one incorrect prediction explanation.
- README includes evaluation summary with key metrics.

### AI Usage and Spec Reflection (2pts)
- Describes at least 2 specific instances of AI tool use.
- Includes a substantive spec reflection with one alignment and one divergence.

## Stretch Features
- +1pt: Inter-Annotator Reliability — agreement rate reported and disagreements analyzed.
- +1pt: Confidence Calibration — relationship between confidence and accuracy described.
- +1pt: Error Pattern Analysis — systematic error pattern identified with evidence.
- +1pt: Deployed Interface — working interface demonstrated.
