"""
Configuration module for prank_line_crafter package.

This module loads environment variables and provides configuration
constants such as API tokens and URLs.

Attributes:
    LLAMA_API_TOKEN (str): The API token for LlamaAPI.
    URL (str): The URL to which the stories will be sent.
"""

import os

from dotenv import load_dotenv

load_dotenv()

LLAMA_API_TOKEN = os.getenv("LLAMA_API_TOKEN")
URL = os.getenv("URL")

if not LLAMA_API_TOKEN or not URL:
    raise ValueError("Missing: LLAMA_API_TOKEN or URL")
