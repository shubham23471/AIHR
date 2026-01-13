"""
Pydantic schemas for skill analysis.
"""
from pydantic import BaseModel


class Skill(BaseModel):
    """Individual skill with metadata."""
    name: str
    category: str
    synonyms: list[str] = []
    implied_skills: list[str] = []


class TechStack(BaseModel):
    """Technology stack categorization."""
    primary: list[str] = []
    secondary: list[str] = []


class SkillAnalysisResponse(BaseModel):
    """Response schema for skill analysis."""
    skills: list[Skill]
    experience_years: int
    seniority_level: str  # junior, mid, senior, lead
    tech_stack: TechStack
    reasoning: str | None = None  # Chain-of-thought from LLM


class SkillAnalysisRequest(BaseModel):
    """Request schema for skill analysis."""
    resume_text: str
