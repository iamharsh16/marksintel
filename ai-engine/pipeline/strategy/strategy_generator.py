"""
Generates marks strategy using frequency data + RAG + LLM.
"""
from pipeline.rag.retriever import retrieve
from pipeline.classifier.prompts import STRATEGY_PROMPT

def generate_strategy(subject_id: str, target_marks: int, strategy_type: str) -> dict:
    # Step 1: Get frequency data from DB
    # Step 2: Retrieve similar questions via RAG
    # Step 3: Build prompt with data
    # Step 4: Call GPT-4o
    # Step 5: Return structured strategy
    pass
