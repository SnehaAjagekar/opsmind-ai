"""
Configuration Module for OpsMind AI.
Loads and validates environment variables.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()


def get_gemini_api_key() -> str:
    """
    Retrieve and validate the Gemini API key from environment variables.
    
    Raises:
        ValueError: If GEMINI_API_KEY is not set or empty.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        raise ValueError(
            "GEMINI_API_KEY is not set or is using the placeholder value. "
            "Please create a .env file based on .env.example and set your actual API key."
        )
    return api_key


def get_model_name() -> str:
    """
    Retrieve the configured Gemini model name with fallback.
    """
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
