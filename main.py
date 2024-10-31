from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode

from src.markdown import extract_markdown_images, extract_markdown_links

def main():
	my_class = TextNode("hello world", TextType.IMAGE, "http://hello.com")
	print(my_class)

	html_node = HTMLNode("p", "This is a paragraph")
	print(f"HTML node: {html_node}")

	leaf_node = LeafNode("This is a paragraph", "p")
	print(f"Leaf node: {leaf_node}")

	children = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

	print(ParentNode('p', children).to_html())

	bold_node = TextNode("Have some BOLD text!", TextType.BOLD)
	print(bold_node.convert_to_html_node().to_html())

	image_node = TextNode("Can you see me?", TextType.IMAGE, "http://spellweaver.com/PhillipXT.jpg")
	print(image_node.convert_to_html_node().to_html())

	split_node = TextNode("This is a text node", TextType.TEXT)
	print(split_node)

	image_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
	images = extract_markdown_images(image_text)
	print(f"Images found: {images}")

	link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
	links = extract_markdown_links(link_text)
	print(f"Links found: {links}")

main()
