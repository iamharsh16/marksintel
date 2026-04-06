"""
Classifies questions using GPT-4o API.
"""
from pipeline.classifier.prompts import CLASSIFICATION_PROMPT

def classify_question(question: str, subject_name: str, syllabus_context: str = "") -> dict:
    # TODO: call OpenAI API with CLASSIFICATION_PROMPT
    pass

def classify_batch(questions: list[str], subject_name: str) -> list[dict]:
    # TODO: classify multiple questions efficiently
    pass
