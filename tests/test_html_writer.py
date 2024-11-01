import unittest

from src.html_writer import extract_title

class TestTextNode(unittest.TestCase):
	def test_eq_markdown_with_header(self):
		markdown = "# Hello\n\n* List Item 1\n* List Item 2"
		header = extract_title(markdown)
		self.assertEqual(header, "Hello")

	def test_eq_markdown_without_header(self):
		markdown = "#Hello"
		self.assertRaises(Exception, lambda: extract_title(markdown))
