"""
OCR-based extraction for scanned PDFs using Tesseract.
"""
from pdf2image import convert_from_path
import pytesseract
import logging

logger = logging.getLogger(__name__)

def extract_text_with_ocr(pdf_path: str, lang: str = "eng+hin") -> str:
    """
    Converts PDF pages to images and extracts text using Tesseract OCR.
    Handles rotated pages and mixed English/Hindi if languages are installed.
    """
    try:
        # Convert pages to images
        images = convert_from_path(pdf_path, dpi=300)
        
        extracted_text = ""
        for i, img in enumerate(images):
            # psm 3 handles fully automatic page segmentation, but not Orientation and Script Detection (OSD)
            # which we can add or leave 3. For rotated pages, psm 1 with osd can be useful.
            # Using psm 1: Automatic page segmentation with OSD. 
            custom_config = r'--oem 3 --psm 1'
            try:
                text = pytesseract.image_to_string(img, lang=lang, config=custom_config)
            except Exception as e:
                logger.warning(f"OCR with OSD failed on page {i}, retrying with basic PSM: {e}")
                custom_config_basic = r'--oem 3 --psm 3'
                text = pytesseract.image_to_string(img, lang=lang, config=custom_config_basic)
                
            extracted_text += f"\n--- Page {i+1} ---\n{text}"
            
        return extracted_text.strip()
    
    except Exception as e:
        logger.error(f"OCR extraction failed for {pdf_path}: {e}")
        raise ValueError(f"Failed to process OCR for document: {e}")
