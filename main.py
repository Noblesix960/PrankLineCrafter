"""
Main module for prank_line_crafter.

This module reads names from a file, generates funny stories using LlamaAPI, 
and sends them to a server.
"""

import sys

from prank_line_crafter.sender import send_story
from prank_line_crafter.story_generator import generate_complete_story


def get_names_from_file(filename):
    """Read names from the specified file.

    Args:
        filename (str): The path to the file containing the names.

    Returns:
        list: A list of names read from the file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:  # Specify encoding
            names = file.readlines()
            return [name.strip() for name in names if name.strip()]
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return []


def main(names_file="names.txt"):
    """Main function to process names and generate/send stories.

    Args:
        names_file (str, optional): The path to the file containing the names. Default: "names.txt".
    """
    names = get_names_from_file(names_file)

    for i, name in enumerate(names, start=1):
        print(f"{i}: Processing {name}... ", end="")

        # Generate a funny story for the current name
        story = generate_complete_story(name)

        # Send the story to the server
        result = send_story(name, story)
        print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
