"""
Splits cleaned text into individual questions.
"""
import re

def segment_questions(cleaned_text: str) -> list[str]:
    """
    Regex-based question segmenter designed to catch SPPU question patterns.
    E.g. "Q. 1", "Q1.", "1.", "1)", "(a)", "a)", etc.
    """
    if not cleaned_text:
        return []

    # Common prefixes indicating a question starts
    # Matches "Q.1", "Q1.", "Q 1 )", "Q. 1.", "1.", "1)", "a)", "(a)", "A.", "A)", "i)", "(i)"
    pattern = r'(?m)^(?:\s*)(?:Q\.?\s*\d+\.?|Q\d+\.?|\d+[\.\)]|\([a-z]\)|[a-z]\)|\([IVXLCDMivxlcdm]+\)|[IVXLCDMivxlcdm]+\))'

    # Findall the starts to split the string
    # We will split on the match, and capturing the matched text back if needed, but 
    # capturing the split regex means the parts will include the match group. 
    # Let's use re.split with a capture group
    
    split_pattern = r'(?m)(^(?:\s*)(?:Q\.?\s*\d+\.?|Q\d+\.?|\d+[\.\)]|\([a-z]\)|[a-z]\)|\([ivxlcdm]+\)|[ivxlcdm]+\))\s*)'
    
    parts = re.split(split_pattern, cleaned_text)
    
    # Parts will be [pre-text, Q_Match1, Q_Body1, Q_Match2, Q_Body2...]
    questions = []
    
    # Ignore initial text if it's not a question (instructions, rubrics)
    # Start iterating through captured matches and their bodies
    # parts[0] is preamble (instructions)
    
    # We rebuild the actual questions: match + body
    for i in range(1, len(parts) - 1, 2):
        q_header = parts[i].strip()
        q_body = parts[i+1].strip()
        
        # Combine
        full_q = f"{q_header} {q_body}".strip()
        if full_q:
            questions.append(full_q)
            
    # Fallback if no questions are found - just return the whole text as 1 block
    if not questions and cleaned_text.strip():
        questions.append(cleaned_text.strip())
        
    return questions
