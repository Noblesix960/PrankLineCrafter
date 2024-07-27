"""
Story generator module for prank_line_crafter package.

This module generates funny stories about a given name using the LlamaAPI.

Functions:
    generate_complete_story(name): Generates a funny story about the given name.
"""

import requests
from llamaapi import LlamaAPI

from .config import LLAMA_API_TOKEN


def generate_complete_story(name):
    """Generate a funny story about the given name using LlamaAPI."""
    llama = LlamaAPI(LLAMA_API_TOKEN)
    api_request_json = {
        "messages": [
            {
                "role": "user",
                "content": f"Generate a funny story about a person named {name}",
            }
        ],
        "max_tokens": 500,
        "stream": False,
    }

    try:
        response = llama.run(api_request_json)
        response.raise_for_status()  # Ensure we notice bad responses
        generated_text = response.json()["choices"][0]["message"]["content"]
        return generated_text
    except requests.exceptions.RequestException as req_err:
        print(f"Request error generating story for {name}: {req_err}")
        return "Story generation failed due to request error."
    except ValueError as val_err:
        print(f"Value error generating story for {name}: {val_err}")
        return "Story generation failed due to value error."
    except KeyError as key_err:
        print(f"Key error generating story for {name}: {key_err}")
        return "Story generation failed due to key error."
