"""
Configuration settings for AIHR backend.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://0.0.0.0:8080/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-32b")
