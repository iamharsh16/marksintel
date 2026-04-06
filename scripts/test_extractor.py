import os
import sys
import logging
from pprint import pprint

# Adjust the path to import from ai-engine directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ai-engine')))

from pipeline.extractor.pdf_extractor import extract_text_from_pdf, is_scanned_pdf
from pipeline.extractor.ocr_extractor import extract_text_with_ocr
from pipeline.extractor.text_cleaner import clean_text
from pipeline.classifier.question_segmenter import segment_questions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory where test PDFs should be placed
TEST_PDF_DIR = os.path.join(os.path.dirname(__file__), 'test_pdfs')

def run_pipeline(pdf_path: str):
    logger.info(f"--- Processing {pdf_path} ---")
    
    try:
        # Check if scanned (falling back to normal logic instead of forcing OCR missing dependencies)
        scanned = is_scanned_pdf(pdf_path)
        logger.info(f"Is Scanned: {scanned}")
        
        # Extract text based on heuristic
        raw_text = ""
        if scanned:
            logger.info("Running OCR extraction...")
            raw_text = extract_text_with_ocr(pdf_path)
        else:
            logger.info("Running standard extraction...")
            try:
                raw_text = extract_text_from_pdf(pdf_path)
            except ValueError:
                logger.info("Standard extraction failed, falling back to OCR...")
                raw_text = extract_text_with_ocr(pdf_path)
        
        # Clean text
        logger.info("Cleaning extracted text...")
        cleaned_text = clean_text(raw_text)
        logger.info(f"Cleaned Text Length: {len(cleaned_text)}")
        
        # Segment Questions
        logger.info("Segmenting questions...")
        questions = segment_questions(cleaned_text)
        logger.info(f"Total Questions Segmented: {len(questions)}")
        
        logger.info("Extracted Questions:")
        for i, q in enumerate(questions):
            logger.info(f"--- Q{i+1} ---\n{q}\n")
            
        print("="*60)
        
    except Exception as e:
        logger.error(f"Error processing {pdf_path}: {e}", exc_info=True)


if __name__ == "__main__":
    if not os.path.exists(TEST_PDF_DIR):
        os.makedirs(TEST_PDF_DIR)
        logger.info(f"Created {TEST_PDF_DIR}. Please drop 5 SPPU PDF papers in this folder and run again.")
        sys.exit(0)
    
    pdf_files = [f for f in os.listdir(TEST_PDF_DIR) if f.lower().endswith('.pdf')]
    if not pdf_files:
        logger.info(f"No PDFs found in {TEST_PDF_DIR}. Please add PDFs and re-run.")
        sys.exit(0)
        
    for pdf_file in pdf_files:
        run_pipeline(os.path.join(TEST_PDF_DIR, pdf_file))