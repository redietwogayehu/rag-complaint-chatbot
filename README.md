# Intelligent Complaint Analysis for Financial Services (RAG System)

## Overview

This project is part of a Retrieval-Augmented Generation (RAG) system designed for CrediTrust Financial to transform large-scale customer complaint data into actionable insights.

The system processes raw consumer complaints from the CFPB dataset and prepares them for semantic search using vector embeddings and a vector database (ChromaDB).

This interim submission covers:
- Exploratory Data Analysis (EDA)
- Data preprocessing and filtering
- Text chunking strategy
- Embedding generation using Sentence Transformers
- Vector database construction using ChromaDB

---

## Business Objective

CrediTrust Financial receives thousands of customer complaints across multiple financial products including:
- Credit Cards
- Personal Loans
- Savings Accounts
- Money Transfers

The goal is to enable internal teams to:
- Quickly identify complaint trends
- Query customer issues in natural language
- Reduce manual analysis time
- Support proactive decision-making

---

## Dataset

Source: Consumer Financial Protection Bureau (CFPB)

The dataset includes:
- Complaint narratives (free-text)
- Product categories
- Issue classifications
- Company metadata
- Submission timestamps

---

## Project Structure


rag-complaint-chatbot/
│
├── data/
│ ├── raw/
│ ├── processed/
│
├── notebooks/
│ └── task1_eda.ipynb
│
├── src/
│ └── build_vectorstore.py
│
├── vector_store/
│ └── chroma_db/ (ignored in git)
│
├── requirements.txt
├── README.md
├── .gitignore


---

## Task 1 — Exploratory Data Analysis & Preprocessing

### Steps performed:
- Loaded CFPB complaint dataset
- Removed records with missing complaint narratives
- Filtered dataset to 4 target product categories:
  - Credit Card
  - Personal Loan
  - Savings Account
  - Money Transfer
- Performed basic EDA on product distribution
- Cleaned text data (normalization, noise removal)

### Key observations:
- Dataset is highly imbalanced across product categories
- Large portion of records lack usable narrative text
- Credit-related complaints dominate dataset volume

---

## Task 2 — Text Chunking, Embedding, and Vector Store

### Sampling Strategy:
- Stratified sampling applied across product categories
- Sampling fraction: 8%
- Final dataset size: ~6,566 complaints

### Text Chunking:
- Chunk size: 500 characters
- Chunk overlap: 50 characters

This ensures semantic continuity across long complaint narratives.

---

### Embedding Model:
- Model: `all-MiniLM-L6-v2`
- Embedding dimension: 384
- Chosen for:
  - Fast CPU performance
  - Strong semantic representation
  - Lightweight architecture suitable for production

---

### Vector Database:
- Tool: ChromaDB
- Persistent storage enabled
- Stores:
  - Embeddings
  - Raw text chunks
  - Metadata (product category, complaint ID)

---

### Ingestion Strategy:
- Large-scale embeddings (~16,131 chunks)
- Batch insertion implemented (batch size: 4000)
- Ensures compliance with ChromaDB ingestion limits

---

## Final Outputs (Interim Stage)

- Filtered complaints: ~6,566
- Total text chunks: ~16,131
- Embedding model: all-MiniLM-L6-v2
- Vector DB: ChromaDB persistent index

