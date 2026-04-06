CLASSIFICATION_PROMPT = """
You are an expert at analysing SPPU university exam question papers.
Given a question, classify it into the following JSON format:

{
  "unit": <unit number 1-6>,
  "topic": "<main topic name>",
  "subtopic": "<specific subtopic>",
  "marks": <marks allotted as integer>,
  "question_type": "<Theory / Numerical / Diagram / Design / Short Answer>",
  "difficulty": "<Easy / Medium / Hard>"
}

Return ONLY valid JSON. No explanation. No markdown.

Question: {question}
Subject: {subject_name}
Syllabus context: {syllabus_context}
"""

STRATEGY_PROMPT = """
You are an expert exam strategist for SPPU university exams.
Based on the following frequency analysis data and historical questions,
generate a marks strategy for a student targeting {target_marks} marks.

Frequency Data:
{frequency_data}

Relevant Historical Questions:
{retrieved_questions}

Return a JSON object with:
{
  "strategy_type": "{strategy_type}",
  "topics": [
    {
      "topic": "<topic name>",
      "unit": <unit number>,
      "priority": <1 = highest>,
      "estimated_marks": <marks>,
      "study_order": <order to study>,
      "reason": "<why this topic>"
    }
  ],
  "total_estimated_marks": <number>,
  "study_advice": "<brief advice>"
}
"""
