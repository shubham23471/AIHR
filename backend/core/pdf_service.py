"""
PDF parsing service using PyMuPDF (fitz).
"""
import fitz  # pymupdf
from pathlib import Path


def parse_pdf_bytes(pdf_bytes: bytes) -> tuple[str, int]:
    """
    Extract text from PDF bytes.
    
    Args:
        pdf_bytes: Raw PDF file bytes
        
    Returns:
        Tuple of (extracted_text, page_count)
    """
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text_parts = []
    
    for page in doc:
        text_parts.append(page.get_text())
    
    doc.close()
    return "\n".join(text_parts), len(text_parts)


def parse_pdf_file(file_path: str | Path) -> tuple[str, int]:
    """
    Extract text from PDF file path.
    
    Args:
        file_path: Path to PDF file
        
    Returns:
        Tuple of (extracted_text, page_count)
    """
    doc = fitz.open(file_path)
    text_parts = []
    
    for page in doc:
        text_parts.append(page.get_text())
    
    doc.close()
    return "\n".join(text_parts), len(text_parts)


def load_resumes_from_directory(directory: str | Path) -> list[dict]:
    """
    Load and parse all PDF resumes from a directory.
    
    Args:
        directory: Path to directory containing PDF files
        
    Returns:
        List of dicts with filename, text, and page_count
    """
    directory = Path(directory)
    resumes = []
    
    for pdf_file in directory.glob("*.pdf"):
        try:
            text, page_count = parse_pdf_file(pdf_file)
            resumes.append({
                "filename": pdf_file.name,
                "text": text,
                "page_count": page_count
            })
        except Exception as e:
            resumes.append({
                "filename": pdf_file.name,
                "text": "",
                "page_count": 0,
                "error": str(e)
            })
    
    return resumes
