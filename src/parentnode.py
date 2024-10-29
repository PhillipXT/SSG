from src.htmlnode import HTMLNode

# A leaf node is an HTML node with no children (eg. <p>Some text with no inner tags</p>)

class ParentNode(HTMLNode):

	# children	Required: The list of child nodes
	# tag		Required: The HTML tag name (p, a, h1, etc.)
	# props		Optional: Dictionary of tag attributes (eg. 'href': 'https://spellweaver.com')

	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if not self.tag:
			raise ValueError("Parent node must have a tag")
		if not self.children:
			raise ValueError("Parent node must have children")

		inner_html = "".join(map(lambda child: child.to_html(), self.children))

		return self.open_tag() + inner_html + self.close_tag()

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.children}, {self.props})"