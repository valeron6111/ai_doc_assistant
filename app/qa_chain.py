from langchain.chains import SimpleSequentialChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from app.embeddings import build_index
import numpy as np
from openai import OpenAI

# Instantiate LLM with deterministic behavior for production usage
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

def retrieve_context(question, index_tuple):
    """
    Perform similarity search over document embeddings to retrieve
    the most relevant context for the given question.
    """
    index, docs = index_tuple
    client = OpenAI()
    q_embedding = np.array(client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    ).data[0].embedding).astype("float32")
    # retrieve top-1 most similar document
    D, I = index.search(np.array([q_embedding]), k=1)
    return docs[I[0][0]]

def generate_answer(question, context):
    """
    Use LangChain's sequential chain to generate LLM response
    based on retrieved context. Prompt templates enforce structured input.
    """
    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template="Using the following context:\n{context}\nAnswer the question: {question}"
    )
    chain = SimpleSequentialChain(chains=[llm], verbose=True)
    return chain.run(prompt.format(question=question, context=context))

def answer_question(question, index_tuple):
    """
    High-level function to answer a user question.
    Combines context retrieval and LLM generation in a clean interface.
    """
    context = retrieve_context(question, index_tuple)
    return generate_answer(question, context)