import re

from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode

from src.markdown_text import text_to_textnodes

from src.markdown_blocks import (
	block_to_blocktype,
	markdown_to_blocks,
	block_type_paragraph,
	block_type_heading,
	block_type_code,
	block_type_quote,
	block_type_ordered_list,
	block_type_unordered_list
)

def markdown_to_html_node(markdown):

	children = []

	markdown = markdown.replace("\t", "")

	# Parse the markdown text into individual blocks
	blocks = markdown_to_blocks(markdown)

	# Loop throug the blocks and determine what type they are
	for block in blocks:
		block_type = block_to_blocktype(block)

		# A paragraph needs to be converted into a list of TextNode, and then into HTMLNode
		if block_type == block_type_paragraph:
			paragraph = " ".join(block.split("\n"))
			kids = list(map(lambda b: b.convert_to_html_node(), text_to_textnodes(paragraph)))
			children.append(ParentNode("p", kids))
		# For a heading, determine the level (h1 to h6, depending on the number of #'s)
		elif block_type == block_type_heading:
			level = len(re.findall(r"^#{1,6}", block))
			text = block[level + 1:]
			kids = list(map(lambda b: b.convert_to_html_node(), text_to_textnodes(text)))
			children.append(ParentNode(f"h{level}", kids))
		elif block_type == block_type_code:
			text = block[3:-3]
			kids = list(map(lambda b: b.convert_to_html_node(), text_to_textnodes(text)))
			children.append(ParentNode("pre", [ParentNode("code", kids)]))
		elif block_type == block_type_quote:
			lines = list(map(lambda n: n.lstrip(">").strip(), block.split("\n")))
			text = " ".join(lines)
			kids = list(map(lambda b: b.convert_to_html_node(), text_to_textnodes(text)))
			children.append(ParentNode("blockquote", kids))
		elif block_type == block_type_ordered_list:
			lines = list(map(lambda n: n[3:], block.split("\n")))
			new_items = []
			for line in lines:
				kids = list(map(lambda b: b.convert_to_html_node(), text_to_textnodes(line)))
				new_items.append(ParentNode("li", kids))
			children.append(ParentNode("ol", new_items))
		elif block_type == block_type_unordered_list:
			lines = list(map(lambda n: n[2:], block.split("\n")))
			new_items = []
			for line in lines:
				kids = list(map(lambda b: b.convert_to_html_node(), text_to_textnodes(line)))
				new_items.append(ParentNode("li", kids))
			children.append(ParentNode("ul", new_items))
		else:
			raise Exception("Invalid block type")

	return ParentNode("div", children)
