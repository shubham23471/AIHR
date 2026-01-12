# Phase 1A: Core Screening Engine

**Scope:** Semantic Skill Analysis (1.4) + Explainable AI Scoring (1.5)  
**Output:** JSON API responses (no UI)  
**Input:** Sample PDF resumes from project folder + hardcoded JD

---

## Prerequisites

- Sample resumes: 4-5 PDFs in `/data/resumes/`
- Sample JD: JSON file at `/data/sample_jd.json`
- LM Studio running locally with DeepSeek-R1-Distill-Qwen-14B (OpenAI-compatible endpoint)
- Virtual environment: `/Users/shubham/saas/aihr/.venv/bin/python`

---

## Tasks

### Task 1: PDF Resume Parsing ⭐ (Priority)

**Deliverable:** Extract structured text from PDF resumes

| Item | Details |
|------|---------|
| PDF reader | Use `pymupdf` (fitz) - fast, no external deps |
| Resume loader | Load all PDFs from `/data/resumes/` directory |
| Text extraction | Convert PDF pages to plain text |
| API endpoint | `POST /api/v1/resumes/parse` accepts PDF, returns extracted text |

---

### Task 2: Project Setup & LLM Integration

**Deliverable:** FastAPI app with working LLM connection

| Item | Details |
|------|---------|
| Pydantic models | `JobDescription`, `Resume`, `Candidate`, `AnalysisResult` |
| LLM service | OpenAI-compatible client pointing to `http://localhost:1234/v1` |
| Config | Environment variables for LLM endpoint, model name |
| Health check endpoint | `GET /health` returning LLM connection status |

---

### Task 3: Semantic Skill Analysis

**Deliverable:** LLM extracts skills as concepts with relationships

| Item | Details |
|------|---------|
| Skill extraction prompt | Extract: skills, experience_years, tech_stack, seniority_level |
| Concept mapping | LLM maps synonyms (e.g., "IaC" → "Infrastructure as Code", "Terraform") |
| Related skills inference | LLM infers implied skills (e.g., "Kubernetes" implies "Docker", "Containers") |
| Structured output | JSON schema enforced via prompt (or function calling if supported) |
| API endpoint | `POST /api/v1/analyze/skills` accepts resume text, returns skill analysis |

**Output Schema:**
```json
{
  "skills": [{"name": "str", "category": "str", "synonyms": ["str"], "implied_skills": ["str"]}],
  "experience_years": 5,
  "seniority_level": "junior | mid | senior | lead",
  "tech_stack": {"primary": ["str"], "secondary": ["str"]}
}
```

---

### Task 4: XAI Scoring Engine

**Deliverable:** Match score with 3-part reasoning + citations

| Item | Details |
|------|---------|
| JD loader | Load sample JD from `/data/sample_jd.json` |
| Match scoring prompt | Compare resume skills vs JD requirements |
| Reasoning sections | Strengths, Gaps, Red Flags (each with citations) |
| Citation format | Quote exact resume text that supports each claim |
| Score calculation | 0-100 based on requirement coverage |
| API endpoint | `POST /api/v1/analyze/match` accepts resume text + JD, returns XAI result |

**Output Schema:**
```json
{
  "match_score": 85,
  "reasoning": {
    "strengths": [{"claim": "str", "citation": "str"}],
    "gaps": [{"requirement": "str", "explanation": "str"}],
    "red_flags": [{"flag": "str", "citation": "str"}]
  },
  "suggested_questions": ["str"],
  "confidence": 0.85
}
```

---

### Task 5: Batch Processing Endpoint

**Deliverable:** Analyze all resumes against JD in one call

| Item | Details |
|------|---------|
| Batch endpoint | `POST /api/v1/analyze/batch` processes all resumes in `/data/resumes/` |
| Response | List of candidates ranked by match_score |
| Include | Full XAI analysis for each candidate |

---

## API Summary

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/health` | Check API status |
| POST | `/api/v1/resumes/parse` | Parse single PDF |
| GET | `/api/v1/resumes/` | List parsed resumes from data folder |
| POST | `/api/v1/analyze/skills` | Semantic skill extraction |
| POST | `/api/v1/analyze/match` | XAI scoring for one resume |
| POST | `/api/v1/analyze/batch` | Analyze all sample resumes |

---

## LLM Recommendation

For local inference with semantic reasoning:
- **Primary:** DeepSeek-R1-Distill-Qwen-14B (Q4_K_M) — good reasoning, runs on 16GB+ VRAM
- **Fallback:** Llama-3.1-8B-Instruct — faster, less VRAM, weaker reasoning
- **Context:** Ensure 8K+ context window for long resumes + JD

---

## Dependencies

```
fastapi
uvicorn
pydantic
pymupdf
openai
python-dotenv
python-multipart
```

---

## File Structure

```
/aihr
├── backend/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           └── resume_routes.py
│   ├── schema/
│   │   └── resume.py
│   ├── core/
│   │   └── pdf_service.py
│   ├── llm/
│   │   └── llm_service.py
│   └── requirements.txt
├── data/
│   ├── resumes/
│   │   └── *.pdf
│   └── sample_jd.json
└── .env
```
