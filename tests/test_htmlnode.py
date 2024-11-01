import unittest

from src.htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
	def test_eq_tag_without_properties(self):
		node = HTMLNode('p', 'This is a paragraph')
		self.assertEqual(node.__repr__(), "HTMLNode(tag: p, value: This is a paragraph, children: None, properties: None)")

	def test_eq_tag_with_properties(self):
		node = HTMLNode('a', 'This is a link', None, {'href': 'http://spellweaver.com'})
		self.assertEqual(node.__repr__(), "HTMLNode(tag: a, value: This is a link, children: None, properties: {'href': 'http://spellweaver.com'})")

	def test_eq_tag_with_children(self):
		node = HTMLNode('p', None, ['a', 'img'], None)
		self.assertEqual(node.__repr__(), "HTMLNode(tag: p, value: None, children: ['a', 'img'], properties: None)")

if __name__ == "__main__":
	unittest.main()