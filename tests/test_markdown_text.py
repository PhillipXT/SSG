import unittest

from src.textnode import TextNode, TextType

from src.markdown_text import (
	text_to_textnodes,
	split_nodes_delimiter,
	split_nodes_images,
	split_nodes_links,
	extract_markdown_images,
	extract_markdown_links
)

class TestMarkdownText(unittest.TestCase):
	def test_eq_plain_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(new_nodes, [TextNode("This is a text node", TextType.TEXT)])

	def test_eq_bold_text(self):
		node = TextNode("This is a node with **bold text**", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(new_nodes, [
			TextNode("This is a node with ", TextType.TEXT),
			TextNode("bold text", TextType.BOLD),
		])

	def test_eq_multiple_bold_text(self):
		node = TextNode("This is a node with **bold text** and some more **bold text**", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertListEqual(new_nodes, [
			TextNode("This is a node with ", TextType.TEXT),
			TextNode("bold text", TextType.BOLD),
			TextNode(" and some more ", TextType.TEXT),
			TextNode("bold text", TextType.BOLD),
		])

	def test_eq_multiple_delimiters(self):
		node = TextNode("This is a node with **bold text** and some *italic text*", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
		self.assertListEqual(new_nodes, [
			TextNode("This is a node with ", TextType.TEXT),
			TextNode("bold text", TextType.BOLD),
			TextNode(" and some ", TextType.TEXT),
			TextNode("italic text", TextType.ITALIC),
		])

	def test_eq_extract_markdown_images(self):
		image_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		images = extract_markdown_images(image_text)
		self.assertListEqual(images, [
			('rick roll', 'https://i.imgur.com/aKaOqIh.gif'),
			('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')
		])

	def test_eq_extract_markdown_links(self):
		link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		links = extract_markdown_links(link_text)
		self.assertListEqual(links, [
			('to boot dev', 'https://www.boot.dev'),
			('to youtube', 'https://www.youtube.com/@bootdotdev'),
		])

	def test_eq_split_nodes_images(self):
		node = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)]
		new_nodes = split_nodes_images(node)
		self.assertListEqual(new_nodes, [
			TextNode('This is text with a ', TextType.TEXT),
			TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
			TextNode(' and ', TextType.TEXT),
			TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'),
		])

	def test_eq_split_nodes_images_with_trailing_text(self):
		node = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)...", TextType.TEXT)]
		new_nodes = split_nodes_images(node)
		self.assertListEqual(new_nodes, [
			TextNode('This is text with a ', TextType.TEXT),
			TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'),
			TextNode(' and ', TextType.TEXT),
			TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'),
			TextNode('...', TextType.TEXT),
		])

	def test_eq_split_nodes_links(self):
		node = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)]
		new_nodes = split_nodes_links(node)
		self.assertListEqual(new_nodes, [
			TextNode('This is text with a link ', TextType.TEXT),
			TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
			TextNode(' and ', TextType.TEXT),
			TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev'),
		])

	def test_eq_text_to_textnodes(self):
		text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		nodes = text_to_textnodes(text)
		self.assertListEqual(nodes, [
			TextNode("This is ", TextType.TEXT),
			TextNode("text", TextType.BOLD),
			TextNode(" with an ", TextType.TEXT),
			TextNode("italic", TextType.ITALIC),
			TextNode(" word and a ", TextType.TEXT),
			TextNode("code block", TextType.CODE),
			TextNode(" and an ", TextType.TEXT),
			TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
			TextNode(" and a ", TextType.TEXT),
			TextNode("link", TextType.LINK, "https://boot.dev"),
		])

if __name__ == "__main__":
	unittest.main()