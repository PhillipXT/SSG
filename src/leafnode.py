from src.htmlnode import HTMLNode

# A leaf node is an HTML node with no children (eg. <p>Some text with no inner tags</p>)

class LeafNode(HTMLNode):

	# value		Required: The value of the HTML tag (eg. the text for a p tag)
	# tag		Optional: The HTML tag name (p, a, h1, etc.); if empty, return raw text
	# props		Optional: Dictionary of tag attributes (eg. 'href': 'https://spellweaver.com')

	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("Leaf node must have a value")
		elif self.tag is None:
			return self.value

		return f"{self.open_tag()}{self.value}{self.close_tag()}"

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"
