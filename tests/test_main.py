import os
import unittest
from unittest.mock import MagicMock, patch

from main import get_names_from_file
from prank_line_crafter.story_generator import generate_complete_story


class TestMain(unittest.TestCase):

    @patch("prank_line_crafter.story_generator.LlamaAPI.run")
    def test_generate_complete_story(self, mock_run):
        # Mock the JSON response of the API call
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {"message": {"content": "Once upon a time, a person named Alice..."}}
            ]
        }
        mock_run.return_value = mock_response

        # Call the function to generate a story
        story = generate_complete_story("Alice")

        # Assert that the generated story contains the expected content
        self.assertIn("Once upon a time, a person named Alice", story)

    def test_get_names_from_file(self):
        # Get the absolute path of names.txt relative to main.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        names_file_path = os.path.join(base_dir, "..", "names.txt")

        # Call the function to read names from the file
        names = get_names_from_file(names_file_path)

        # Assert that the names list matches the expected list
        self.assertEqual(names, ["Alice", "Bob", "Charlie"])


if __name__ == "__main__":
    unittest.main()
