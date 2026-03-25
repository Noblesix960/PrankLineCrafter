"""
Sender module for prank_line_crafter package.

This module contains functions to send generated stories to a server.

Functions:
    send_story(name, story): Sends the generated story to the server.
"""

import requests

from .config import URL


def send_story(name, story):
    """Send the generated story to the server.

    Args:
        name (str): The name of the person the story is about.
        story (str): The generated story content.

    Returns:
        str: The result of the request, indicating success or failure.
    """
    data = {
        "wnd_ShortTextField_670972831": name,
        "wnd_RadioGroupField_714859850": "wnd_RadioGroupOption_74325105",
        "wnd_LongTextField_230983133": story,
        "send": "wnd_FormBlock_2860052",
    }

    try:
        response = requests.post(URL, data=data, timeout=10)
        response.raise_for_status()  # Ensure we notice bad responses
        if response.status_code == 200:
            return "Request sent successfully"
        return f"Error in request: Status code {response.status_code}"
    except requests.RequestException as http_error:
        return f"Request failed: {http_error}"
