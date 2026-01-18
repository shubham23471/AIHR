"""
Pydantic schemas for XAI scoring and match analysis.
"""
from pydantic import BaseModel, Field


class Strength(BaseModel):
    """Individual strength with citation from resume."""
    claim: str = Field(..., description="What the candidate is strong at")
    citation: str = Field(..., description="Exact quote from resume supporting this claim")


class Gap(BaseModel):
    """Missing or weak requirement."""
    requirement: str = Field(..., description="JD requirement that is missing or weak")
    explanation: str = Field(..., description="Why this is a gap or how it's insufficient")


class RedFlag(BaseModel):
    """Concerning pattern or discrepancy."""
    flag: str = Field(..., description="The concerning pattern or issue")
    citation: str = Field(..., description="Exact quote from resume showing this issue")


class Reasoning(BaseModel):
    """Structured reasoning for match score."""
    strengths: list[Strength] = Field(default_factory=list, description="Candidate strengths aligned with JD")
    gaps: list[Gap] = Field(default_factory=list, description="Missing or weak requirements")
    red_flags: list[RedFlag] = Field(default_factory=list, description="Concerning patterns or discrepancies")


class MatchScoreResponse(BaseModel):
    """Response schema for XAI match scoring."""
    match_score: int = Field(..., ge=0, le=100, description="Overall match score (0-100)")
    reasoning: Reasoning = Field(..., description="Detailed reasoning with citations")
    suggested_questions: list[str] = Field(default_factory=list, description="Interview questions based on gaps/flags")
    confidence: float = Field(..., ge=0.0, le=1.0, description="AI confidence in this assessment (0.0-1.0)")


class MatchScoreRequest(BaseModel):
    """Request schema for match scoring."""
    resume_text: str = Field(..., min_length=1, description="Plain text content of the resume")
    jd_text: str | None = Field(None, description="Job description text (defaults to sample JD if not provided)")


class JobDescription(BaseModel):
    """Schema for job description data."""
    jd: str = Field(..., description="Job description text")
