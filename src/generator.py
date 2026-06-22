from transformers import pipeline

# lightweight local LLM alternative (no API needed)
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_answer(prompt: str) -> str:
    try:
        result = generator(
            prompt,
            max_length=256,
            do_sample=False
        )
        return result[0]["generated_text"]

    except Exception as e:
        return f"Generation error: {str(e)}"