"""
Retrieves semantically similar questions for a given query.
"""
from pipeline.rag.embedder import embed_text
from pipeline.rag.vector_store import search_similar

def retrieve(query: str, top_k: int = 10) -> list[dict]:
    query_embedding = embed_text(query)
    return search_similar(query_embedding, top_k)
