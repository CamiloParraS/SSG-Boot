from main import extract_tittle
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

class TestExtractTittle(unittest.TestCase):
    def test_extract_tittle_with_title(self):
        md_content = "# My Title\n\nThis is some content."
        title = extract_tittle(md_content)
        self.assertEqual(title, "My Title")

    def test_extract_tittle_without_title(self):
        md_content = "This is some content without a title."
        with self.assertRaises(Exception) as context:
            extract_tittle(md_content)
        self.assertEqual(str(context.exception), "No title found in the markdown content.")

    def test_extract_tittle_with_multiple_titles(self):
        md_content = "# First Title\n\nSome content.\n\n# Second Title"
        title = extract_tittle(md_content)
        self.assertEqual(title, "First Title")
    
    def test_extract_tittle_with_empty_title(self):
        md_content = "# \n\nThis is some content."
        title = extract_tittle(md_content)
        self.assertEqual(title, "")

    def test_extract_tittle_with_whitespace_title(self):
        md_content = "#    \n\nThis is some content."
        title = extract_tittle(md_content)
        self.assertEqual(title, "")

    def test_extract_title_second_level_heading(self):
        md_content = "## Second Level Heading\n\nThis is some content."
        with self.assertRaises(Exception) as context:
            extract_tittle(md_content)
        self.assertEqual(str(context.exception), "No title found in the markdown content.")

    def test_extract_title_with_tittle_in_second_line(self):
        md_content = "Some content.\n# Title in second line"
        with self.assertRaises(Exception) as context:
            extract_tittle(md_content)
        self.assertEqual(str(context.exception), "No title found in the markdown content.")

if __name__ == "__main__":
    unittest.main()