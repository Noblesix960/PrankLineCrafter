# PrankLineCrafter

PrankLineCrafter is a Python script that generates humorous stories based on names provided in a text file and submits these stories to a server via HTTP POST requests. The stories are generated using the LlamaAPI, which is integrated into the script to create engaging and amusing content.

## Features

- Reads names from a `names.txt` file.
- Generates a funny story for each name using the LlamaAPI.
- Sends each name and its corresponding story to a specified server URL via HTTP POST requests.
- Handles environment variables for sensitive information such as API tokens and server URLs.

## Requirements

- Python 3.6 or higher
- `requests` library
- `llamaapi` library
- `python-dotenv` library

## Setup

To set up and run the script, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the repository with the following content:

    ```plaintext
    LLAMA_API_TOKEN=your_llama_api_token
    URL=your_target_url
    ```

   Replace `your_llama_api_token` with your LlamaAPI token and `your_target_url` with the URL of the server where you want to send the generated stories.

## Usage

1. Prepare a `names.txt` file in the root directory with one name per line.

2. Run the `llm.py` script:

    ```bash
    python llm.py
    ```

   The script will read names from `names.txt`, generate a story for each name, and send the results to the specified URL.

## Configuration

- **LLAMA_API_TOKEN**: Your LlamaAPI token for accessing the API.
- **URL**: The target server URL where the POST requests will be sent.

## Error Handling

- If the `names.txt` file is missing, the script will notify you with an error message.
- If the server responds with an error, the script will print the status code for debugging purposes.

## Example

Given a `names.txt` file with the following content:
```plaintext
Alice
Bob
Charlie
```

The script will generate and send stories for "Alice", "Bob", and "Charlie" to the specified server.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.
