import torch
import gradio as gr
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

MODEL_PATH = "./model"
ID2LABEL = {0: "People", 1: "Objects", 2: "Systems", 3: "Ideas"}

try:
    tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
    model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()
    MODEL_LOADED = True
except Exception:
    MODEL_LOADED = False


def classify(post: str):
    if not MODEL_LOADED:
        return (
            "Model not found — save your fine-tuned model to ./model/ first.",
            "—",
            {label: 0.0 for label in ID2LABEL.values()},
        )

    if not post or not post.strip():
        return "Enter a post above.", "—", {label: 0.0 for label in ID2LABEL.values()}

    inputs = tokenizer(
        post, return_tensors="pt", truncation=True, max_length=128, padding=True
    )
    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=-1)[0]
    predicted_id = int(probs.argmax())
    label = ID2LABEL[predicted_id]
    confidence = float(probs[predicted_id])
    all_scores = {ID2LABEL[i]: round(float(probs[i]), 4) for i in range(4)}

    return label, f"{confidence:.1%}", all_scores


demo = gr.Interface(
    fn=classify,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Paste a Reddit post here...",
        label="Post",
    ),
    outputs=[
        gr.Textbox(label="Predicted Label"),
        gr.Textbox(label="Confidence"),
        gr.Label(num_top_classes=4, label="All Label Scores"),
    ],
    title="TakeMeter — r/unpopularopinion Classifier",
    description=(
        "Classifies posts from r/unpopularopinion into one of four categories: "
        "**People**, **Objects**, **Systems**, or **Ideas**."
    ),
    examples=[
        ["We need to stop idolizing celebrities and start appreciating regular people."],
        ["Vanilla doesn't belong in the bathroom."],
        ["Going to university isn't worth it anymore."],
        ["Unconditional love is the biggest lie."],
        ["Excess noise levels that you or your property creates should be subject to a year end tax."],
    ],
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch()
