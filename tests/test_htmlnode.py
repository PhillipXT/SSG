import unittest

from src.htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
	def test_eq_tag_without_properties(self):
		node = HTMLNode('p', 'This is a paragraph')
		self.assertEqual(str(node), '<p>This is a paragraph</p>')

	def test_eq_tag_with_properties(self):
		node = HTMLNode('a', 'This is a link', None, {'href': 'http://spellweaver.com'})
		self.assertEqual(str(node), '<a href="http://spellweaver.com">This is a link</a>')

	def test_eq_tag_with_children(self):
		node = HTMLNode('p', None, ['a', 'img'], None)
		self.assertEqual(str(node), '<p>a/img</p>')

if __name__ == "__main__":
	unittest.main()