import requests
from llamaapi import LlamaAPI
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve the Llama API token from the environment variables
llama_api_token = os.getenv("LLAMA_API_TOKEN")

# Initialize the LlamaAPI SDK with the API token
llama = LlamaAPI(llama_api_token)

def generate_complete_story(name):
    # Construct the API request to generate a funny story
    api_request_json = {
        "messages": [
            {"role": "user", "content": f"Generate a funny story about a person named {name}."}
        ],
        "max_tokens": 500,  # Set the maximum number of tokens to get a short story
        "stream": False
    }

    # Execute the API request
    response = llama.run(api_request_json)

    # Extract the generated text from the API response
    generated_text = response.json()["choices"][0]["message"]["content"]

    return generated_text

def get_names_from_file(filename):
    try:
        with open(filename, 'r') as file:
            names = file.readlines()
            return [name.strip() for name in names]  # Remove whitespace and newline characters
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return []

# Read names from the names.txt file
names = get_names_from_file('names.txt')

# URL of the target server
url = os.getenv("URL")

# Iterate through each name in the list and send a request to the server
for i, name in enumerate(names, start=1):
    print(f"{i}: ", end="")
    
    # Generate a funny story for the current name
    story = generate_complete_story(name)
    
    # Form data to send with the POST request
    data = {
        "wnd_ShortTextField_670972831": name,
        "wnd_RadioGroupField_714859850": "wnd_RadioGroupOption_74325105",
        "wnd_LongTextField_230983133": story,
        "send": "wnd_FormBlock_2860052"
    }

    # Send the POST request to the server
    response = requests.post(url, data=data)

    # Check the status of the response and print an appropriate message
    if response.status_code == 200:
        print("Request sent successfully")
    else:
        print("Error in request")
        print("Status code:", response.status_code)
