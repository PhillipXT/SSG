import unittest

from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node1 = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node1, node2)

	def test_type_not_eq(self):
		node1 = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.ITALIC)
		self.assertNotEqual(node1, node2)

	def test_text_not_eq(self):
		node1 = TextNode("This is not a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node1, node2)

	def test_url_eq(self):
		node1 = TextNode("This is a text node", TextType.BOLD, None)
		node2 = TextNode("This is a text node", TextType.BOLD, None)
		self.assertEqual(node1, node2)

	def test_url_not_eq(self):
		node1 = TextNode("This is a text node", TextType.BOLD, None)
		node2 = TextNode("This is a text node", TextType.BOLD, "http://hello.com")
		self.assertNotEqual(node1, node2)

	def test_convert_to_html_node(self):
		node = TextNode("Plain raw text here!", TextType.NORMAL)
		self.assertEqual(node.convert_to_html_node().to_html(), "Plain raw text here!")

	def test_convert_to_html_node(self):
		node = TextNode("Have some BOLD text!", TextType.BOLD)
		self.assertEqual(node.convert_to_html_node().to_html(), "<b>Have some BOLD text!</b>")

	def test_convert_to_html_node(self):
		node = TextNode("Click here NOW!", TextType.LINK, "http://spellweaver.com")
		self.assertEqual(node.convert_to_html_node().to_html(), '<a href="http://spellweaver.com">Click here NOW!</a>')

	def test_convert_to_html_node(self):
		node = TextNode("Can you see me?", TextType.IMAGE, "http://spellweaver.com/PhillipXT.jpg")
		self.assertEqual(node.convert_to_html_node().to_html(), '<img src="http://spellweaver.com/PhillipXT.jpg" alt="Can you see me?"></img>')

if __name__ == "__main__":
	unittest.main()