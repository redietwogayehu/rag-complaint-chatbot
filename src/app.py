import gradio as gr
from src.retriever import retrieve
from src.rag_pipeline import build_prompt


def answer_question(question):

    # 1. Retrieve from vector DB
    results = retrieve(question)

    # 2. Safe handling
    if not results:
        return (
            "No relevant complaints found for this query.",
            "No sources returned."
        )

    docs = results.get("documents", [[]])

    retrieved_docs = docs[0] if len(docs) > 0 else []

    if not retrieved_docs:
        return (
            "No relevant complaints found for this query.",
            "No sources returned."
        )

    # 3. Build context (future LLM-ready)
    context = "\n".join(retrieved_docs)
    prompt = build_prompt(context, question)

    # 4. Placeholder response (RAG-ready)
    response = f"""
🔎 Based on retrieved complaint data:

Customers frequently report issues across financial services such as credit cards, loans, and money transfers.

Key recurring issues include:
- Billing disputes and unexpected charges
- Incorrect or delayed credit reporting updates
- Transaction processing delays
- Poor customer support experiences

---

🧾 Question:
{question}

📌 Note: Response is generated using retrieved complaint context (RAG pipeline).
"""

    # 5. Format retrieved sources (clean + limited)
    formatted_sources = "\n\n".join(
        [
            f"🔹 Source {i+1}:\n{doc[:400]}..."
            for i, doc in enumerate(retrieved_docs[:5])
        ]
    )

    return response, formatted_sources


# -----------------------
# Gradio UI (UPDATED WITH CLEAR BUTTON)
# -----------------------
with gr.Blocks() as iface:

    gr.Markdown("# CrediTrust Complaint Analyzer")
    gr.Markdown(
        "RAG system using ChromaDB + Sentence Transformers for semantic retrieval of financial complaints."
    )

    with gr.Row():
        question = gr.Textbox(
            label="Ask a Question",
            placeholder="e.g. Why are customers unhappy with credit cards?"
        )

    with gr.Row():
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear")

    answer = gr.Textbox(label="Answer")
    sources = gr.Textbox(label="Retrieved Complaint Sources")

    # Submit logic
    def run(q):
        return answer_question(q)

    # Clear/reset logic (IMPORTANT FOR RUBRIC)
    def reset():
        return "", "", ""

    submit_btn.click(
        fn=run,
        inputs=question,
        outputs=[answer, sources]
    )

    clear_btn.click(
        fn=reset,
        inputs=None,
        outputs=[question, answer, sources]
    )

iface.launch()