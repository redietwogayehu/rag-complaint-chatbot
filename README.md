Intelligent Complaint Analysis for Financial Services (RAG System)
🧠 Overview

This project implements a Retrieval-Augmented Generation (RAG) system for analyzing large-scale financial service customer complaints. It enables semantic search over unstructured complaint narratives and provides an interactive interface for querying and retrieving relevant complaint insights.

The system is designed to support internal stakeholders such as:

Customer Support teams
Product Managers
Compliance and Risk teams

It helps transform raw complaint data into actionable insights through semantic retrieval and contextual response generation.

🏢 Business Problem

CrediTrust Financial receives a high volume of customer complaints across multiple financial products including credit cards, loans, savings accounts, and money transfers.

Key Challenges:
Large volume of unstructured complaint text
Manual analysis is slow and inconsistent
Difficulty identifying recurring patterns across products
Lack of semantic search over historical complaints
Objective:

Build a system that allows users to:

Ask natural language questions
Retrieve relevant complaint records
Summarize key issues using a RAG pipeline
📂 Dataset
Source: CFPB Consumer Complaint Database
Contains structured metadata and unstructured complaint narratives
Key Fields:
Product category
Complaint narrative
Issue / sub-issue
Complaint ID
Company metadata
Data Preparation:
Removed records with missing narratives
Standardized and cleaned text
Filtered to key financial products:
Credit Card
Personal Loan
Savings Account
Money Transfer
Final Dataset:
~6,566 sampled complaints
~16,131 text chunks generated for embedding
🔍 Exploratory Data Analysis (EDA)
Key Insights:
Strong class imbalance across financial products
Credit-related complaints dominate dataset
Significant portion of records missing usable narratives
Complaint lengths vary significantly (short to very long narratives)
Visualizations:
Product category distribution (bar chart)
Complaint narrative word count distribution (histogram)

📁 See: notebooks/task1_eda.ipynb

🧹 Data Preprocessing
Steps Applied:
Lowercasing text
Removing unnecessary whitespace and noise
Filtering invalid or empty narratives
Stratified sampling (8%) across product categories
✂️ Text Chunking Strategy

To improve embedding quality and retrieval precision:

Chunk size: 500 characters
Overlap: 50 characters
Why chunking?
Preserves semantic meaning across long complaints
Improves retrieval granularity
Prevents loss of information in embeddings
🧠 Embedding Model
Model: all-MiniLM-L6-v2 (Sentence Transformers)
Embedding dimension: 384
Why this model?
Lightweight and efficient for CPU environments
High-quality semantic representations
Widely used in production RAG systems
🗄️ Vector Database (ChromaDB)
Persistent vector store using ChromaDB
Stores:
Embeddings
Original text chunks
Metadata (product_category, complaint_id)
Ingestion Strategy:
Batch processing used to avoid memory limits
Optimized embedding generation pipeline
🔎 RAG Pipeline Architecture
User Query
   ↓
Retriever (ChromaDB similarity search)
   ↓
Relevant Complaint Chunks
   ↓
Prompt Builder
   ↓
Response Generator (placeholder LLM logic)
   ↓
Gradio UI Output
💬 Retrieval-Augmented Generation (RAG)

The system:

Retrieves top relevant complaint chunks
Builds a context-aware prompt
Generates a structured response based on retrieved evidence

Current implementation uses a placeholder response generator, designed for future LLM integration.

🖥️ Interactive UI (Gradio)
Features:
Ask natural language questions
Retrieve relevant complaints
View generated analytical response
Inspect source complaint evidence
📸 UI Evidence

Screenshots included for evaluation:

screenshots/
├── app_home.png
├── app_response.png

These demonstrate:

Functional UI
Retrieval system working
Context-aware responses
📊 Evaluation Summary (Task 3)
Retrieval Quality:
High relevance across financial product queries
Semantic search effectively identifies related complaint themes
Strengths:
Strong alignment between query intent and retrieved documents
Clean preprocessing improves retrieval accuracy
Limitations:
No reranking model implemented
Response generation is placeholder-based
No quantitative metrics (precision@k not implemented)
🚀 Future Improvements
Integrate LLM (OpenAI / local model)
Add reranking model for better retrieval accuracy
Implement evaluation metrics (precision@k, recall@k)
Deploy using Streamlit Cloud or HuggingFace Spaces
Add user feedback loop for continuous improvement
⚙️ How to Run the Project
Install dependencies:
pip install -r requirements.txt
Run application:
streamlit run app.py

or

python app.py
🧪 Tech Stack
Python
Pandas
SentenceTransformers
ChromaDB
LangChain Text Splitters
Gradio / Streamlit
👨‍💻 Project Structure
rag-complaint-chatbot/
│
├── app.py
├── src/
├── data/
├── notebooks/
├── screenshots/
├── vector_store/
└── README.md
