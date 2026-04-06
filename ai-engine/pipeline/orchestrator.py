"""
Master pipeline runner.
Coordinates: extract → segment → classify → analyse → embed → store
"""

def run_pipeline(pdf_path: str, paper_id: str, subject_id: str):
    # Step 1: Extract text from PDF
    # Step 2: Segment into individual questions
    # Step 3: Classify each question with LLM
    # Step 4: Save to PostgreSQL
    # Step 5: Generate embeddings and store in vector DB
    # Step 6: Run frequency analysis
    # Step 7: Update paper status to completed
    pass
