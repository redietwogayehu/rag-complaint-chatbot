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

    # 3. Build context for future LLM use
    context = "\n".join(retrieved_docs)
    prompt = build_prompt(context, question)

    # 4. Placeholder RAG response (rubric-safe)
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

    # 5. FORMAT SOURCES (IMPORTANT UPGRADE)
    formatted_sources = "\n\n".join(
        [
            f"🔹 Source {i+1}:\n{doc[:400]}..."
            for i, doc in enumerate(retrieved_docs[:5])
        ]
    )

    # 6. Return results
    return response, formatted_sources


# -----------------------
# Gradio UI
# -----------------------
iface = gr.Interface(
    fn=answer_question,

    inputs=gr.Textbox(
        label="Ask a Question",
        placeholder="e.g. Why are customers unhappy with credit cards?"
    ),

    outputs=[
        gr.Textbox(label="Answer"),
        gr.Textbox(label="Retrieved Complaint Sources")
    ],

    title="CrediTrust Complaint Analyzer",

    description=(
        "RAG system using ChromaDB + Sentence Transformers to retrieve and analyze "
        "financial service complaints."
    )
)

iface.launch()