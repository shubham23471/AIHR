"""
Analysis API routes for skill extraction and scoring.
"""
from fastapi import APIRouter, HTTPException

from schema.analysis import SkillAnalysisRequest, SkillAnalysisResponse
from schema.scoring import MatchScoreRequest, MatchScoreResponse
from core.analysis_service import analyze_skills
from core.scoring_service import calculate_match_score, load_job_description

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


@router.post("/match", response_model=MatchScoreResponse)
async def analyze_match(request: MatchScoreRequest):
    """
    Calculate XAI match score between resume and job description.
    
    Provides explainable AI scoring with:
    - Match score (0-100)
    - Detailed reasoning (strengths, gaps, red flags)
    - Citations from resume for all claims
    - Suggested interview questions
    - Confidence score
    
    If no JD is provided, uses the sample JD from /data/sample_jd.json
    """
    if not request.resume_text.strip():
        raise HTTPException(status_code=400, detail="Resume text cannot be empty")
    
    try:
        # Load JD if not provided
        jd_text = request.jd_text
        if not jd_text:
            jd_text = load_job_description()
        
        # Calculate match score
        result = calculate_match_score(request.resume_text, jd_text)
        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Match analysis failed: {str(e)}")
