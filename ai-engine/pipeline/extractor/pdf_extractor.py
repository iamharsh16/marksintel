"""
PDF text extraction using pdfplumber and PyMuPDF.
Handles: digital PDFs, multi-page, table extraction.
"""
import pdfplumber
import fitz  # PyMuPDF
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def is_scanned_pdf(pdf_path: str, threshold: int = 50) -> bool:
    """
    Checks if a PDF is scanned by evaluating the amount of real text on first few pages.
    Returns True if the document appears to be scanned or contains little real text.
    """
    text_length = 0
    try:
        # Check up to first 3 pages
        with fitz.open(pdf_path) as doc:
            for i in range(min(3, len(doc))):
                page = doc[i]
                text_length += len(page.get_text())
                if text_length > threshold:
                    return False
    except Exception as e:
        logger.error(f"Error checking if {pdf_path} is scanned: {e}")
        return True # Fallback to true if reading fails

    return True # If text length remains <= threshold

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text attempting pdfplumber first, then PyMuPDF as fallback.
    If the document is effectively scanned, raises ValueError.
    """
    if is_scanned_pdf(pdf_path):
        raise ValueError("Document is scanned. OCR required.")

    # Try pdfplumber first with layout preservation to fix intermingled watermarks 
    # and column overlapping common in SPPU papers
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                # Use extract_text with x_tolerance and layout parameters tuned
                page_text = page.extract_text(x_tolerance=2, y_tolerance=2, layout=True)
                if page_text:
                    text += page_text + "\n"
        
        if text.strip():
            return text.strip()
    except Exception as e:
        logger.warning(f"pdfplumber extraction failed: {e}")

    # Fallback to PyMuPDF
    try:
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"
        
        if text.strip():
            return text.strip()
    except Exception as e:
        logger.warning(f"PyMuPDF extraction failed: {e}")

    raise ValueError("Failed to extract digital text from the document.")
