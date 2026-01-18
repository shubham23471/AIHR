"""
Scoring service for XAI match analysis between resumes and job descriptions.
"""
import json
import re
from pathlib import Path

from llm.llm_service import llm_service
from schema.scoring import MatchScoreResponse, JobDescription


# Load prompts from files
PROMPTS_DIR = Path(__file__).parent.parent / "prompts"
DATA_DIR = Path(__file__).parent.parent.parent / "data"


def load_prompt(filename: str) -> str:
    """Load a prompt from the prompts directory."""
    prompt_path = PROMPTS_DIR / filename
    return prompt_path.read_text()


def load_job_description() -> str:
    """
    Load the sample job description from /data/sample_jd.json.
    
    Returns:
        Job description text
    """
    jd_path = DATA_DIR / "sample_jd.json"
    
    if not jd_path.exists():
        raise FileNotFoundError(f"Job description not found at {jd_path}")
    
    with open(jd_path, 'r') as f:
        data = json.load(f)
    
    # Parse the JobDescription schema
    jd_obj = JobDescription(**data)
    return jd_obj.jd


def extract_think_and_json(response: str) -> tuple[str | None, str]:
    """
    Extract chain-of-thought from <think> tags and JSON from the response.
    
    DeepSeek-R1 distill models output (with known issue of missing opening tag):
    reasoning here...
    </think>
    {json output}
    
    Returns:
        Tuple of (reasoning, json_string)
    """
    reasoning = None
    json_str = response.strip()
    
    # Check if there's a closing </think> tag (model often omits opening tag)
    if "</think>" in response:
        # Split on closing tag
        parts = response.split("</think>", 1)
        reasoning = parts[0].strip()
        json_str = parts[1].strip()
        
        # If there was an opening tag, remove it from reasoning
        if reasoning.startswith("<think>"):
            reasoning = reasoning[7:].strip()  # Remove "<think>"
    
    # Try to extract JSON object from the string (handles cases with extra text)
    json_match = re.search(r'(\{[\s\S]*\})', json_str)
    if json_match:
        json_str = json_match.group(1)
    
    # Clean up JSON if it's in a code block
    if json_str.startswith("```"):
        lines = json_str.split("\n")
        # Remove first line (```json) and last line (```)
        json_str = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])
    
    return reasoning, json_str


def calculate_match_score(resume_text: str, jd_text: str) -> MatchScoreResponse:
    """
    Calculate XAI match score between resume and job description.
    
    Args:
        resume_text: Plain text content of the resume
        jd_text: Job description text
        
    Returns:
        MatchScoreResponse with score, reasoning, questions, and confidence
    """
    system_prompt = load_prompt("xai_scoring.txt")
    
    user_message = f"""RESUME:
{resume_text}

---

JOB DESCRIPTION:
{jd_text}

---

Analyze the match between this resume and job description."""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    
    # Use lower temperature for more consistent scoring
    response = llm_service.chat(messages, temperature=0.2)
    
    # Extract chain-of-thought and JSON
    reasoning, json_str = extract_think_and_json(response)
    
    try:
        data = json.loads(json_str)
        return MatchScoreResponse(**data)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"LLM returned invalid JSON: {e}\n"
            f"JSON string: {json_str[:500]}\n"
            f"Full response: {response[:1000]}"
        )
    except Exception as e:
        raise ValueError(
            f"Failed to parse LLM response: {e}\n"
            f"JSON string: {json_str[:500]}\n"
            f"Full response: {response[:1000]}"
        )
