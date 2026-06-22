def build_prompt(context, question):
    return f"""
You are a financial complaint analyst.

Use the context below to answer the question.

Context:
{context}

Question:
{question}

Provide a clear, structured summary of customer issues.
"""