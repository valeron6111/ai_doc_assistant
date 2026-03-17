import faiss
import numpy as np
from openai import OpenAI
from app.utils import load_docs

client = OpenAI()

def embed_text(texts):
    """
    Generate vector embeddings for a list of texts using OpenAI embeddings API.
    Returns a numpy array of type float32, compatible with FAISS.
    """
    embeddings = []
    for t in texts:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=t
        )
        embeddings.append(response.data[0].embedding)
    return np.array(embeddings).astype("float32")

def build_index(folder="docs"):
    """
    Build a FAISS vector index from all documents in a folder.
    This index can be used for similarity search for LLM context retrieval.
    """
    docs = load_docs(folder)
    embeddings = embed_text(docs)
    index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance metric
    index.add(embeddings)
    return index, docs