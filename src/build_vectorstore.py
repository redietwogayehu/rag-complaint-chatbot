import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# -----------------------
# 1. Load dataset
# -----------------------
df = pd.read_csv("data/processed/filtered_complaints.csv")

# -----------------------
# 1.1 Normalize columns (IMPORTANT FIX)
# -----------------------
df.columns = df.columns.str.strip()

# -----------------------
# 2. Safety check
# -----------------------
required_cols = ["product_category", "clean_text", "Complaint ID"]
missing = [c for c in required_cols if c not in df.columns]

if missing:
    raise ValueError(f"Missing columns: {missing}")

# -----------------------
# 3. Stratified sampling (SAFE)
# -----------------------
sample_df = (
    df.groupby("product_category", group_keys=False)
      .sample(frac=0.08, random_state=42)
      .reset_index(drop=True)
)

print("Sample size:", sample_df.shape)

# -----------------------
# 4. Chunking setup
# -----------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# -----------------------
# 5. Build documents
# -----------------------
documents = []

for _, row in sample_df.iterrows():
    chunks = splitter.split_text(row["clean_text"])

    for chunk in chunks:
        documents.append({
            "text": chunk,
            "product_category": row["product_category"],
            "complaint_id": row["Complaint ID"]
        })

print("Total chunks:", len(documents))

# -----------------------
# 6. Embedding model
# -----------------------
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# -----------------------
# 7. ChromaDB setup (safe reuse)
# -----------------------
client = chromadb.PersistentClient(
    path="vector_store/chroma_db"
)

collection = client.get_or_create_collection(
    name="complaints"
)

# -----------------------
# 8. Batch embeddings (optimized)
# -----------------------
texts = [d["text"] for d in documents]

embeddings = model.encode(
    texts,
    show_progress_bar=True,
    batch_size=128,   # upgraded speed
    convert_to_numpy=True
).tolist()

# -----------------------
# 9. Store in vector DB (BATCH SAFE)
# -----------------------
BATCH_SIZE = 4000  # safe for ChromaDB limits

for i in range(0, len(documents), BATCH_SIZE):

    batch_docs = documents[i:i+BATCH_SIZE]
    batch_texts = [d["text"] for d in batch_docs]
    batch_embeddings = embeddings[i:i+BATCH_SIZE]

    collection.add(
        ids=[str(j) for j in range(i, i + len(batch_docs))],
        embeddings=batch_embeddings,
        documents=batch_texts,
        metadatas=[
            {
                "product_category": d["product_category"],
                "complaint_id": d["complaint_id"]
            }
            for d in batch_docs
        ]
    )

    print(f"Inserted batch {i} → {i + len(batch_docs)}")
# -----------------------
# 10. Verification
# -----------------------
print("Vector DB built successfully")
print("Total vectors stored:", collection.count())