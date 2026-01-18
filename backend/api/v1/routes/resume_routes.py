"""
Resume parsing API routes.
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

from schema.resume import ResumeParseResponse, ResumeListResponse, ResumeListItem
from core.pdf_service import parse_pdf_bytes, load_resumes_from_directory

router = APIRouter(prefix="/api/v1/resumes", tags=["resumes"])

# Data directory path (relative to project root)
DATA_DIR = Path(__file__).parent.parent.parent.parent.parent / "data" / "resumes"


@router.post("/parse", response_model=ResumeParseResponse)
async def parse_resume(file: UploadFile = File(...)):
    """
    Parse a single PDF resume and extract text.
    
    Args:
        file: Uploaded PDF file
        
    Returns:
        Extracted text with metadata
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted")
    
    try:
        contents = await file.read()
        text, page_count = parse_pdf_bytes(contents)
        
        return ResumeParseResponse(
            filename=file.filename,
            page_count=page_count,
            text=text,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse PDF: {str(e)}")


@router.get("/", response_model=ResumeListResponse)
async def list_resumes():
    """
    List and parse all resumes from the data directory.
    
    Returns:
        List of parsed resumes with preview text
    """
    if not DATA_DIR.exists():
        raise HTTPException(status_code=404, detail="Resumes directory not found")
    
    resumes_data = load_resumes_from_directory(DATA_DIR)
    
    resumes = [
        ResumeListItem(
            filename=r["filename"],
            page_count=r["page_count"],
            text_preview=r["text"] if r["text"] else ""
        )
        for r in resumes_data
    ]
    
    return ResumeListResponse(resumes=resumes, total=len(resumes))
