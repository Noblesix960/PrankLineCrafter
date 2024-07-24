import requests
from .config import URL


def send_story(name, story):
    """Send the generated story to the server."""
    data = {
        "wnd_ShortTextField_670972831": name,
        "wnd_RadioGroupField_714859850": "wnd_RadioGroupOption_74325105",
        "wnd_LongTextField_230983133": story,
        "send": "wnd_FormBlock_2860052"
    }

    try:
        response = requests.post(URL, data=data)
        response.raise_for_status()  # Ensure we notice bad responses
        if response.status_code == 200:
            return "Request sent successfully"
        else:
            return f"Error in request: Status code {response.status_code}"
    except requests.RequestException as e:
        return f"Request failed: {e}"
