from prank_line_crafter.story_generator import generate_complete_story
from prank_line_crafter.sender import send_story
import sys


def get_names_from_file(filename):
    """Read names from the specified file."""
    try:
        with open(filename, 'r') as file:
            names = file.readlines()
            return [name.strip() for name in names if name.strip()]
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return []


def main(names_file='names.txt'):
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
