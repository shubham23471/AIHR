"""
Configuration settings for AIHR backend.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
# LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:1234/v1")
# LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-r1-distill-qwen-14b")

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://127.0.0.1:8000/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "neuralmagic/DeepSeek-R1-Distill-Qwen-7B-quantized.w8a8")



