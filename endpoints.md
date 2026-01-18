# AIHR API Endpoints

## Server

Start the server:
```bash
python -m uvicorn main:app --reload --port 8001 --app-dir backend
```

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | API health check |
| GET | `/health/llm` | LLM connection check |
| POST | `/api/v1/resumes/parse` | Parse PDF resume |
| GET | `/api/v1/resumes/` | List resumes from data folder |
| POST | `/api/v1/analyze/skills` | Semantic skill analysis |

---

## Sample Requests

### Health Check
```bash
curl http://localhost:8001/health
```

### LLM Health Check
```bash
curl http://localhost:8001/health/llm
```

### Parse PDF Resume
```bash
curl -X POST "http://localhost:8001/api/v1/resumes/parse" \
  -F "file=@data/resumes/Shubham_SR_DE_2025.pdf"
```

### List Resumes
```bash
curl http://localhost:8001/api/v1/resumes/
```

### Skill Analysis
```bash
curl -X POST "http://localhost:8001/api/v1/analyze/skills" \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "John Doe\nSenior Software Engineer at Google (2020-Present)\n\nSkills: Python, Java, Kubernetes, Docker, GCP, PostgreSQL\n\nExperience:\n- Led team of 5 engineers\n- Built microservices architecture\n- Implemented CI/CD pipelines\n\nPrevious: Software Engineer at Facebook (2018-2020)\n\nEducation: MS Computer Science, Stanford 2018"
  }'
```

**Expected Response:**
```json
{
  "skills": [
    {"name": "Python", "category": "Programming", "synonyms": [], "implied_skills": ["pip", "venv"]},
    {"name": "Kubernetes", "category": "DevOps", "synonyms": ["K8s"], "implied_skills": ["Docker", "YAML"]}
  ],
  "experience_years": 6,
  "seniority_level": "senior",
  "tech_stack": {
    "primary": ["Python", "Java", "Kubernetes"],
    "secondary": ["PostgreSQL", "GCP"]
  },
  "reasoning": "Let me analyze this resume... The candidate has 6 years of experience (2018-2024)... They led a team which indicates senior level..."
}
```

> **Note:** The `reasoning` field contains the chain-of-thought from DeepSeek-R1's `<think>` tags.