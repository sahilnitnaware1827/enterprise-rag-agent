# Enterprise RAG Agent

An Enterprise-grade Retrieval-Augmented Generation (RAG) application built with **FastAPI**, **LangGraph**, **LangChain**, **Google Gemini**, and **FAISS**. The system allows users to upload one or more PDF documents and ask natural language questions based only on the uploaded knowledge base.

---

## Features

* Upload one or multiple PDF documents
* Automatic document ingestion pipeline
* PDF parsing using PyPDF
* Intelligent document chunking
* Sentence Transformer embeddings
* FAISS vector database
* Incremental indexing (new PDFs are added without rebuilding the entire database)
* LangGraph-powered AI agent
* Google Gemini LLM integration
* Conversation memory
* Source citations (document name and page number)
* Application logging
* REST API built with FastAPI

---

## Tech Stack

### AI & LLM

* LangChain
* LangGraph
* Google Gemini
* Sentence Transformers

### Backend

* FastAPI
* Uvicorn

### Vector Database

* FAISS

### Document Processing

* PyPDF

### Utilities

* Python
* Python Dotenv

---

## Project Structure

```text
enterprise-rag-agent/

├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
├── db/
│
└── src/
    ├── chat_service.py
    ├── chunker.py
    ├── embedding.py
    ├── graph.py
    ├── ingestion.py
    ├── llm.py
    ├── loader.py
    ├── logger.py
    ├── memory.py
    ├── prompts.py
    ├── retrieval.py
    ├── routes.py
    ├── tools.py
    ├── upload_service.py
    ├── utils.py
    └── vectorstore.py
```

---

## System Architecture

```text
PDF Upload
      │
      ▼
PDF Loader
      │
      ▼
Document Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
LangGraph Agent
      │
      ▼
Google Gemini
      │
      ▼
Answer + Source Citations
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Returns application health status.

---

### Upload PDF

```http
POST /upload
```

Uploads one or more PDF files, processes them, generates embeddings, and updates the FAISS vector database.

---

### Chat

```http
POST /chat
```

Example Request

```json
{
    "question": "What is the leave policy?"
}
```

Example Response

```json
{
    "answer": "Employees receive 20 paid leaves annually.\n\nSources:\n- Employee_Handbook.pdf (Page 12)"
}
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the project

```bash
cd enterprise-rag-agent
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=your_google_api_key
```

Run the application

```bash
uvicorn app:app --reload
```

Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Workflow

1. Upload one or more PDF documents.
2. The ingestion pipeline extracts text and creates document chunks.
3. Chunks are converted into vector embeddings.
4. Embeddings are stored in a FAISS vector database.
5. User submits a question.
6. Relevant document chunks are retrieved.
7. LangGraph agent combines retrieved context with the Gemini model.
8. The assistant returns an answer along with source citations.

---

## Future Improvements

* Document deletion
* Re-indexing support
* Metadata filtering
* User authentication
* Cloud deployment
* Docker support

---

## Author

**Sahil Nitnaware**

AI / ML Engineer | Generative AI | LangGraph | RAG | FastAPI | Python
