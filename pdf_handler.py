import pdfplumber
from pdf2image import convert_from_path
import pytesseract

def extract_text(pdf_path):
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        if len(text.strip()) > 100:
            return text
    except:
        pass

    # OCR fallback
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text
