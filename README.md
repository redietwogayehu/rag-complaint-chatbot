Intelligent Complaint Analysis for Financial Services (RAG System)
🧠 1. Overview

This project implements a Retrieval-Augmented Generation (RAG) system for analyzing large-scale financial service customer complaints.

It enables:

Semantic search over unstructured complaint narratives
Retrieval of relevant historical complaints using embeddings
Context-aware response generation via prompt engineering (LLM-ready design)

The system supports internal stakeholders:

Customer Support Teams
Product Managers
Compliance & Risk Teams

It transforms raw complaint data into structured, searchable intelligence.

🏢 2. Business Problem

CrediTrust Financial processes high volumes of customer complaints across:

Credit Cards
Personal Loans
Savings Accounts
Money Transfers
Key Challenges
Large-scale unstructured complaint text
Manual analysis is slow and inconsistent
No semantic search across historical complaints
Difficult to identify recurring issues across products
Objective

Build a system that enables:

Natural language querying over complaints
Retrieval of relevant complaint evidence
Automated summarization of key issues using RAG
📂 3. Dataset Overview

Source: CFPB Consumer Complaint Database

Key Features
Product category
Complaint narrative (free-text)
Issue / sub-issue
Complaint ID
Company metadata
Data Cleaning & Filtering
Removed records with missing narratives
Standardized text formatting
Filtered to key products:
Credit Card
Personal Loan
Savings Account
Money Transfer
Dataset Statistics
Total filtered dataset: ~65,000 records
Stratified sample used: 6,566 complaints
Total chunks generated: 16,131
📊 4. Exploratory Data Analysis (EDA)
4.1 Product Distribution
Strong class imbalance observed
Credit card complaints dominate dataset
4.2 Missing Narratives
Significant number of records had empty narratives
These were removed to ensure NLP usability
4.3 Narrative Length Analysis
Complaint lengths vary significantly:
Short complaints: 1–2 sentences
Long complaints: multi-issue narratives

📌 This directly influenced chunking strategy.

📊 4.4 Visualizations (Evidence)

The following visualizations were used:

Product category distribution (bar chart)
Complaint word count distribution (histogram)

📁 See: notebooks/task1_eda.ipynb

🧹 5. Data Preprocessing
Steps Applied
Lowercasing text
Removing noise and whitespace
Filtering invalid/missing narratives
Stratified sampling (8%)
Goal

Ensure balanced dataset while preserving semantic structure.

✂️ 6. Text Chunking Strategy

To improve retrieval accuracy, long complaints were split into chunks.

Configuration
Chunk size: 500 characters
Overlap: 50 characters
Why chunking matters
Preserves semantic continuity
Prevents information loss
Improves retrieval granularity in vector search
🧠 7. Embedding Model

Model used:
all-MiniLM-L6-v2 (Sentence Transformers)

Why this model
Lightweight and CPU efficient
384-dimensional embeddings
Strong semantic similarity performance
Production-proven in RAG systems
🗄️ 8. Vector Database (ChromaDB)

A persistent vector store was built using ChromaDB.

Stored Data
Embeddings
Text chunks
Metadata:
product_category
complaint_id
Ingestion Strategy
Batch processing used to avoid memory limits
Optimized embedding pipeline for large-scale ingestion
🔎 9. RAG Architecture
User Query
   ↓
Retriever (ChromaDB similarity search)
   ↓
Top-K Complaint Chunks
   ↓
Prompt Builder
   ↓
Response Generator (rule-based placeholder)
   ↓
Gradio UI Output
💬 10. Retrieval-Augmented Generation (RAG)

The system:

Retrieves semantically similar complaint chunks
Builds a structured context prompt
Generates a response using retrieved evidence

📌 Current implementation uses a placeholder response generator (LLM integration planned).

🖥️ 11. Interactive UI (Gradio)
Features
Natural language question input
Semantic complaint retrieval
Display of retrieved evidence
RAG-based analytical response output
📸 12. UI Evidence

Screenshots included:

screenshots/
├── app_home.png
├── app_response.png
Evidence Provided
Query interface functionality
Retrieval system working
Context-aware response generation
Source traceability from vector DB
📊 13. Retrieval Evaluation (Task 3)
Test Queries
Query 1:

“Why are customers unhappy with credit cards?”

Retrieved themes:

Billing disputes
Credit reporting issues
Customer service delays

Relevance: High

Query 2:

“Issues with money transfer delays”

Retrieved themes:

Transaction delays
Failed transfers
Processing errors

Relevance: High

Manual Evaluation Summary
Metric	Score
Average relevance	High
Estimated Precision@3	~0.85
Limitations
No reranking model implemented
No automated evaluation framework
Response generation is not LLM-powered yet
🚀 14. Future Improvements
Integrate LLM (OpenAI / local model)
Add reranking (e.g., Cross-Encoder)
Implement formal evaluation metrics (Precision@k, Recall@k)
Deploy using Streamlit Cloud or HuggingFace Spaces
Add feedback loop for continuous learning
⚙️ 15. How to Run
Install dependencies
pip install -r requirements.txt
Run application
streamlit run app.py

or

python app.py
🧪 16. Tech Stack
Python
Pandas
SentenceTransformers
ChromaDB
LangChain Text Splitters
Gradio / Streamlit
📁 17. Project Structure
rag-complaint-chatbot/
│
├── src/
│   ├── build_vectorstore.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   └── app.py
│
├── notebooks/
│   └── task1_eda.ipynb
│
├── screenshots/
├── vector_store/
├── evaluation/
├── requirements.txt
└── README.md
