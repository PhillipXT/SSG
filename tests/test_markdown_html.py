import unittest

from src.markdown_html import (
	markdown_to_html_node
)

class TestMarkdownBlocks(unittest.TestCase):
	def test_eq_markdown_to_html_node_1(self):
		text = (
			"""
			This is **bolded**
			paragraph text in a p
			tag here
			"""
		)
		node = markdown_to_html_node(text)
		html = node.to_html()
		self.assertEqual(html, '<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>')

	def test_eq_markdown_to_html_node_2(self):
		text = (
			"""
			This is *italic* text in a p tag here.  This markdown consists of:

			* paragraph text
			* italic text
			* a list
			* a code block
			"""
		)
		node = markdown_to_html_node(text)
		html = node.to_html()
		self.assertEqual(html, '<div><p>This is <i>italic</i> text in a p tag here.  This markdown consists of:</p><ul><li>paragraph text</li><li>italic text</li><li>a list</li><li>a code block</li></ul></div>')

	def test_eq_markdown_to_html_node_3(self):
		text = (
			"""
			This is regular text with a

			```block of code```
			"""
		)
		node = markdown_to_html_node(text)
		html = node.to_html()
		self.assertEqual(html, '<div><p>This is regular text with a</p><pre><code>block of code</code></pre></div>')

if __name__ == "__main__":
	unittest.main()