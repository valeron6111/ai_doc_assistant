from fastapi import FastAPI, UploadFile
from app.utils import save_file
from app.embeddings import build_index
from app.qa_chain import answer_question

app = FastAPI()

# Initialize document index on startup
# Using global index_tuple to maintain state; for production, consider async updates or caching
index_tuple = build_index()

@app.post("/upload")
async def upload_file(file: UploadFile):
    """
    Endpoint to upload new documents.
    Rebuilds the vector index after every upload.
    In production, this should be async or batched for performance.
    """
    path = save_file(await file.read(), file.filename)
    global index_tuple
    index_tuple = build_index()  # rebuild index after new document
    return {"filename": file.filename, "status": "uploaded"}

@app.get("/ask")
def ask(question: str):
    """
    Endpoint to ask a question.
    Retrieves relevant context from documents and generates an LLM response.
    """
    answer = answer_question(question, index_tuple)
    return {"question": question, "answer": answer}