# 🤖 OpsMind AI — Business Operations Copilot

OpsMind AI is an AI-powered business assistant that combines **Retrieval-Augmented Generation (RAG)**, **LLMs**, **vector search**, and **business data analytics** to answer questions about company policies and business performance.

The system intelligently routes user questions to the appropriate tool — either a document-based RAG pipeline or a business data analytics pipeline.

---

## 🚀 Features

- 📄 **Document Question Answering**
  - Answers questions from company policy documents
  - Uses Retrieval-Augmented Generation (RAG)
  - Retrieves relevant document chunks using FAISS

- 🧠 **LLM Integration**
  - Uses Google Gemini for natural-language responses
  - Grounds document answers using retrieved business information

- 🔎 **Semantic Search**
  - Generates embeddings using Sentence Transformers
  - Uses FAISS for vector similarity search

- 📊 **Business Data Analytics**
  - Processes CSV business data using Pandas
  - Calculates sales, orders, cancellations, returns, regions, and categories

- 🔀 **Intelligent Question Routing**
  - Routes policy/document questions to the RAG pipeline
  - Routes business-data questions to the analytics pipeline

- ⚡ **Direct Numerical Analysis**
  - Exact business metrics are calculated directly using Pandas
  - Avoids unnecessary LLM calls for deterministic calculations

- 🖥️ **Interactive Streamlit Interface**
  - Simple web interface for interacting with the AI assistant
  - Displays answers and retrieved document information

---

## 🏗️ Architecture

```text
                         User Question
                              │
                              ▼
                       ┌──────────────┐
                       │    Router    │
                       └──────┬───────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
        Document Question            Business Question
                │                           │
                ▼                           ▼
          RAG Pipeline                Pandas Analytics
                │                           │
                ▼                           ▼
        Sentence Transformers          Business Data
                │                           │
                ▼                           ▼
             FAISS                   Exact Calculations
                │                           │
                ▼                           │
             Gemini                       │
                │                           │
                └─────────────┬─────────────┘
                              ▼
                         Final Answer