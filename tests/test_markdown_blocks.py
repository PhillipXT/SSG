import unittest

from src.textnode import TextNode, TextType

from src.markdown_blocks import (
	markdown_to_blocks,
	block_to_blocktype,
	block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote
)

class TestMarkdownBlocks(unittest.TestCase):
	def test_eq_blocktype_is_heading(self):
		block_type = block_to_blocktype("### This is a heading")
		self.assertEqual(block_type, block_type_heading)

	def test_eq_blocktype_is_not_heading_1(self):
		block_type = block_to_blocktype("####### This is not a heading")
		self.assertNotEqual(block_type, block_type_heading)

	def test_eq_blocktype_is_not_heading_2(self):
		block_type = block_to_blocktype("##_# This is not a heading")
		self.assertNotEqual(block_type, block_type_heading)

	def test_eq_blocktype_is_code_single_line(self):
		block_type = block_to_blocktype("```This is a code block```")
		self.assertEqual(block_type, block_type_code)

	def test_eq_blocktype_is_code_multi_line(self):
		block_type = block_to_blocktype("```This is a code block\nwith two lines```")
		self.assertEqual(block_type, block_type_code)

	def test_eq_blocktype_is_not_code(self):
		block_type = block_to_blocktype("```This is not a code block")
		self.assertNotEqual(block_type, block_type_code)

	def test_eq_blocktype_is_quote(self):
		block_type = block_to_blocktype(">This is the text\n>of a quote.")
		self.assertEqual(block_type, block_type_quote)

	def test_eq_blocktype_is_not_quote(self):
		block_type = block_to_blocktype(">This is the text\nof a paragraph.")
		self.assertNotEqual(block_type, block_type_quote)

	def test_eq_blocktype_is_ordered_list(self):
		block_type = block_to_blocktype("1. Item One\n2. Item Two\n3. Item Three")
		self.assertEqual(block_type, block_type_ordered_list)

	def test_eq_blocktype_is_not_ordered_list(self):
		block_type = block_to_blocktype("1. Item One\n2. Item Two\n3 - Item Three")
		self.assertNotEqual(block_type, block_type_ordered_list)

	def test_eq_blocktype_is_unordered_list(self):
		block_type = block_to_blocktype("* Item One\n* Item Two\n* Item Three")
		self.assertEqual(block_type, block_type_unordered_list)

	def test_eq_blocktype_is_not_unordered_list(self):
		block_type = block_to_blocktype("* Item One\n* Item Two\nItem Three")
		self.assertNotEqual(block_type, block_type_unordered_list)

	def test_eq_blocktype_is_paragraph(self):
		block_type = block_to_blocktype("This is just a normal paragraph.")
		self.assertEqual(block_type, block_type_paragraph)

	def test_eq_markdown_to_blocks(self):
		text = (
			"""
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.
This is a sentence in the same paragraph, but on a new line.

* This is the first list item in a list block
* This is a list item
* This is another list item
			"""
		)
		blocks = markdown_to_blocks(text)
		self.assertListEqual(blocks, [
			'# This is a heading',
			'This is a paragraph of text. It has some **bold** and *italic* words inside of it.\nThis is a sentence in the same paragraph, but on a new line.',
			'* This is the first list item in a list block\n* This is a list item\n* This is another list item'
		])

if __name__ == "__main__":
	unittest.main()