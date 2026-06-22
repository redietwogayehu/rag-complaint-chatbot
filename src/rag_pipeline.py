def build_prompt(context, question):

    return f"""
You are a financial complaint analyst.

Use ONLY the context below.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""