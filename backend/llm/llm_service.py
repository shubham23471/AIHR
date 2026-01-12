"""
LLM service for interacting with local LLM (OpenAI-compatible API).
"""
from openai import OpenAI
from config import LLM_BASE_URL, LLM_MODEL


class LLMService:
    """Service for LLM interactions using OpenAI-compatible API."""
    
    def __init__(self):
        self.client = OpenAI(
            base_url=LLM_BASE_URL,
            api_key="not-needed"  # Local LLM doesn't require API key
        )
        self.model = LLM_MODEL
    
    def chat(self, messages: list[dict], temperature: float = 0.7) -> str:
        """
        Send a chat completion request to the LLM.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Sampling temperature (0-1)
            
        Returns:
            LLM response content as string
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    
    def check_health(self) -> dict:
        """
        Check if the LLM service is reachable.
        
        Returns:
            Dict with status and model info
        """
        try:
            # Simple test message
            response = self.chat(
                messages=[{"role": "user", "content": "Say 'ok' and nothing else."}],
                temperature=0
            )
            return {
                "status": "connected",
                "model": self.model,
                "base_url": LLM_BASE_URL,
                "test_response": response[:50] if response else None
            }
        except Exception as e:
            return {
                "status": "error",
                "model": self.model,
                "base_url": LLM_BASE_URL,
                "error": str(e)
            }


# Singleton instance
llm_service = LLMService()
