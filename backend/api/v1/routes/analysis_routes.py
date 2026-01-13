"""
Analysis API routes for skill extraction and scoring.
"""
from fastapi import APIRouter, HTTPException

from schema.analysis import SkillAnalysisRequest, SkillAnalysisResponse
from core.analysis_service import analyze_skills

router = APIRouter(prefix="/api/v1/analyze", tags=["analysis"])


@router.post("/skills", response_model=SkillAnalysisResponse)
async def analyze_resume_skills(request: SkillAnalysisRequest):
    """
    Analyze resume text and extract structured skill information.
    
    Returns semantic skill analysis including:
    - Skills with categories, synonyms, and implied skills
    - Experience years
    - Seniority level
    - Tech stack breakdown
    """
    if not request.resume_text.strip():
        raise HTTPException(status_code=400, detail="Resume text cannot be empty")
    
    try:
        result = analyze_skills(request.resume_text)
        return result
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
