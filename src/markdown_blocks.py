import re

from functools import reduce

# These are the currently supported block types:
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ordered_list = "ordered_list"
block_type_unordered_list = "unordered_list"

# Break the text down into blocks and return a list of text-based blocks.  Blocks are defined by being separated by a blank line.
# Inputs:	text		=> raw text of the markdown file
# Output:	A list of blocks, which contain the raw text of the block
def markdown_to_blocks(text):
	filtered_blocks = []

	blocks = text.split("\n\n")

	for block in blocks:
		if block != "":
			filtered_blocks.append(block.strip())

	return filtered_blocks

# Evaluate the text of a block and return the type.  Currently supported are paragraph/heading/code/quote/olist/ulist
# Inputs:	block_text	=> The raw markdown text of a block
# Output:	A string identifying the type of the block.
def block_to_blocktype(block_text):

	lines = block_text.split("\n")

	if len(re.findall(r"^#{1,6} ", block_text)) > 0:
		return block_type_heading

	# Code blocks must start and end with [```]
	if block_text[0:3] == '```' and block_text[-3:] == "```":
		return block_type_code
	
	# For a quote block, every line must start with [>]	
	if block_text.startswith(">"):
		if reduce(lambda x, line: x & (line[0] == ">") , lines, True):
			return block_type_quote
		else:
			return block_type_paragraph
	
	# For an unordered list, every line must start with [* ] or [- ]
	if block_text.startswith(("* ", "- ")):
		if reduce(lambda x, line: x & ((line[0:2] == "* ") or (line[0:2] == "- ")) , lines, True):
			return block_type_unordered_list

	# For an ordered list, every line must start with a number, followed by [. ], with numbers
	# starting at 1 and incrementing by 1 on every subsequent line
	if block_text.startswith("1. "):
		for i in range(0, len(lines)):
			if not lines[i].startswith(f"{i + 1}. "):
				return block_type_paragraph

		return block_type_ordered_list

	return block_type_paragraph
