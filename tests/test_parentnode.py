import unittest

from src.parentnode import ParentNode
from src.leafnode import LeafNode

class TestParentNode(unittest.TestCase):

	children = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

	def test_eq_no_tag(self):
		node = ParentNode(None, self.children)
		self.assertRaises(ValueError, lambda: node.to_html())

	def test_eq_no_children(self):
		node = ParentNode('p', None)
		self.assertRaises(ValueError, lambda: node.to_html())

if __name__ == "__main__":
	unittest.main()