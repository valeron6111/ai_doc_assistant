# AI Document Assistant – Production Ready

## Project Description

AI Document Assistant is a production-ready AI helper for searching information in documents and answering questions using LLM.

The project demonstrates:

- LLM integration (GPT-4 / OpenAI API) for answer generation
- Vector document search via FAISS
- Chain orchestration (LangChain-like) and graph visualization of processing (LangGraph)
- FastAPI for frontend or other service integration
- Cloud deployment readiness (Docker + AWS / Azure)

## Features

- Document upload (.txt) via API
- Document indexing and vector store creation
- Relevant document search by user query
- Answer generation with LLM
- Processing chain visualization (LangGraph-like)

## Tech Stack

- Python 3.11, FastAPI
- OpenAI GPT / LLaMA / MPT
- LangChain + LangGraph (networkx)
- FAISS for vector search
- Docker for production packaging
- Cloud services: AWS SageMaker, Azure OpenAI, S3 / Blob Storage

## Project Structure

```
ai_doc_assistant/
├── app/
│   ├── main.py          # FastAPI application
│   ├── embeddings.py    # document vectorization
│   ├── qa_chain.py      # search + LLM chain
│   ├── graph.py         # chain visualization
│   └── utils.py         # file handling
├── docs/                # text documents
├── requirements.txt
├── Dockerfile
└── README.md
```

## Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
uvicorn app.main:app --reload
```

Via Docker:

```bash
docker build -t ai_doc_assistant .
docker run -p 8000:8000 ai_doc_assistant
```

### API

**Upload file:**

```
POST http://localhost:8000/upload
```

**Ask a question:**

```
GET http://localhost:8000/ask?question=Where is order #1234?
```

## Cloud Deployment

1. Create model endpoint in AWS SageMaker / Azure OpenAI Service
2. Update `qa_chain.py` with the cloud endpoint
3. Build Docker image → push to AWS ECR / Azure ACR
4. Deploy via ECS / App Service / Kubernetes
5. Connect S3 / Blob Storage for persistent document storage
