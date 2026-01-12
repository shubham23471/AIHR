"""
Pydantic schemas for resume parsing.
"""
from pydantic import BaseModel


class ResumeParseResponse(BaseModel):
    """Response schema for parsed resume."""
    filename: str
    page_count: int
    text: str
    status: str = "success"


class ResumeListItem(BaseModel):
    """Schema for resume list item."""
    filename: str
    page_count: int
    text_preview: str  # First 500 chars


class ResumeListResponse(BaseModel):
    """Response schema for listing resumes."""
    resumes: list[ResumeListItem]
    total: int
