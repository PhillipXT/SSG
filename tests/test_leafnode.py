import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
	def test_eq_tag_without_properties(self):
		node = LeafNode('p', 'This is a paragraph')
		self.assertEqual(node.to_html(), '<p>This is a paragraph</p>')

	def test_eq_tag_with_properties(self):
		node = LeafNode('a', 'This is a link', {'href': 'http://spellweaver.com'})
		self.assertEqual(node.to_html(), '<a href="http://spellweaver.com">This is a link</a>')

	def test_eq_no_tag(self):
		node = LeafNode(None, 'This is just plain text')
		self.assertEqual(node.to_html(), 'This is just plain text')

	def test_error_no_value(self):
		node = LeafNode('p', None, None)
		self.assertRaises(ValueError, lambda: node.to_html())

if __name__ == "__main__":
	unittest.main()