from functools import reduce

class HTMLNode:

	# Tag		No tag = raw text
	# Value		No value = assume children
	# Children	No children = assume value
	# Props		No props = no attributes

	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag					# Optional: The HTML tag name (p, a, h1, etc.)
		self.value = value				# Optional: The value of the HTML tag (eg. the text for a p tag)
		self.children = children		# Optional: List of child HTMLNode objects
		self.props = props				# Optional: Dictionary of tag attributes (eg. 'href': 'https://spellweaver.com')

	def to_html(self):
		raise NotImplementedError("Subclass must implement to_html() method")
	
	def open_tag(self):
		return "<" + self.tag + self.props_to_html() + ">"
	
	def close_tag(self):
		return "</" + self.tag + ">"

	def props_to_html(self):
		
		if self.props is None:
			return ""
		
		result = ""
		
		for key, value in self.props.items():
			result += f' {key}="{value}"'
		
		return result

	def children_to_string(self):
		return "" if not self.children else reduce(lambda x, y: x + "/" + y, self.children)

	def __repr__(self):
		return f"<{self.tag}{self.props_to_html()}>{self.value if self.value else self.children_to_string()}</{self.tag}>"
