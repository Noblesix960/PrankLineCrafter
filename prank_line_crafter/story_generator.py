from llamaapi import LlamaAPI
from .config import LLAMA_API_TOKEN


def generate_complete_story(name):
    """Generate a funny story about the given name using LlamaAPI."""
    llama = LlamaAPI(LLAMA_API_TOKEN)
    api_request_json = {
        "messages": [
            {"role": "user",
             "content": f"Generate a funny story about a person named {name}"}
        ],
        "max_tokens": 500,
        "stream": False
    }

    try:
        response = llama.run(api_request_json)
        response.raise_for_status()  # Ensure we notice bad responses
        generated_text = response.json()["choices"][0]["message"]["content"]
        return generated_text
    except Exception as e:
        print(f"Error generating story for {name}: {e}")
        return "Story generation failed."
