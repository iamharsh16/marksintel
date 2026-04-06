"""
Cleans raw extracted text: removes headers, footers,
page numbers, fixes encoding issues.
"""
import re

def clean_text(raw_text: str) -> str:
    """
    Cleans OCR'd or extracted text from SPPU question papers.
    Handles extra whitespace, common header/footer artifacts, 
    seat No blocks prominently found in SPPU papers, and encoding bugs.
    """
    if not raw_text:
        return ""

    # Fix basic encoding issues/normalize unicode
    text = raw_text.encode("utf-8", "ignore").decode("utf-8")
    
    # Common SPPU headers/footers to strip
    # Remove strings like "SAVITRIBAI PHULE PUNE UNIVERSITY"
    # Or common footers like "[Total No. of Printed Pages: X]"
    patterns_to_remove = [
        r"\[Total No\.? of Printed Pages[^\]]*\]",
        r"\[Total No\.? of Questions[^\]]*\]",
        r"Seat\s*No\.?[_\.\s:]*",  # Seat no box
        r"P\.T\.O\.?",
        r"\(?PTO\)?",
        r"--- Page \d+ ---",
        r"^\s*Page \d+ of \d+\s*$",
    ]
    
    # Process line by line or on whole text
    # Clean out known patterns multi-line or block
    for pattern in patterns_to_remove:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE | re.MULTILINE)
        
    # Remove lines having only 1 or 2 isolated characters (often resulting from vertical watermarks)
    # Exclude lines that look like valid question starts like "1)", "a)", "Q1", "[8]"
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Pre-compress internal spaces so length checks work correctly!
        s = re.sub(r'\s+', ' ', line.strip())
        
        # Keep empty lines to preserve paragraphs, but we will compress them later anyway
        if not s:
            cleaned_lines.append(line)
            continue
        
        # If it's a very short line (e.g., watermark digits "8 3" or "2 -")
        if len(s) <= 4:
            # Check if it's a valid question marker or mark notation like '1)', '(a)', '8M', '[8]'
            if re.match(r'^(\d+[\)\.]|[a-z][\)\.]|\([a-z]\)|\[\d+\]|\d+\s*[Mm])$', s, re.IGNORECASE):
                cleaned_lines.append(line)
            elif s in ["or", "OR", "Or"]:
                cleaned_lines.append(line)
            else:
                # Vertical watermark artifact - skip it
                continue
        else:
            cleaned_lines.append(line)
            
    text = '\n'.join(cleaned_lines)

    # Clean multiple spaces and multiple newlines
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Strip whitespace from edges
    return text.strip()
