"""
Analysis service for semantic skill extraction using LLM.
"""
import json
import re
from pathlib import Path

from llm.llm_service import llm_service
from schema.analysis import SkillAnalysisResponse


# Load prompts from files
PROMPTS_DIR = Path(__file__).parent.parent / "prompts"


def load_prompt(filename: str) -> str:
    """Load a prompt from the prompts directory."""
    prompt_path = PROMPTS_DIR / filename
    return prompt_path.read_text()


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


def analyze_skills(resume_text: str) -> SkillAnalysisResponse:
    """
    Analyze resume text and extract structured skill information.
    
    Args:
        resume_text: Plain text content of the resume
        
    Returns:
        SkillAnalysisResponse with extracted skills, metadata, and reasoning
    """
    system_prompt = load_prompt("skill_analysis.txt")
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Analyze this resume:\n\n{resume_text}"}
    ]
    
    response = llm_service.chat(messages, temperature=0.1)
    # print("="*100)
    # print(response)
    # print("="*100)
    
    # Extract chain-of-thought and JSON
    reasoning, json_str = extract_think_and_json(response)
    
    try:
        data = json.loads(json_str)
        # Add reasoning to the response
        data["reasoning"] = reasoning
        return SkillAnalysisResponse(**data)
    except json.JSONDecodeError as e:
        raise ValueError(f"LLM returned invalid JSON: {e}\nJSON string: {json_str[:500]}\nFull response: {response[:1000]}")

