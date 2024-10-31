import re

from src.textnode import TextType, TextNode

def text_to_textnodes(text):
	nodes = [TextNode(text, TextType.TEXT)]
	nodes = split_nodes_images(nodes)
	nodes = split_nodes_links(nodes)
	nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
	nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
	nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
	return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []

	for node in old_nodes:
		if node.text_type == TextType.TEXT:
			sections = node.text.split(delimiter)

			if len(sections) % 2 == 0:
				raise Exception(f"No closing mark found for {delimiter}")

			for i in range(0, len(sections)):
				if sections[i] == "":
					continue
				elif i % 2 == 0:
					new_nodes.append(TextNode(sections[i], TextType.TEXT))
				else:
					new_nodes.append(TextNode(sections[i], text_type))
		else:
			new_nodes.append(node)

	return new_nodes

def split_nodes_images(old_nodes):
	new_nodes = []

	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue

		image_list = extract_markdown_images(node.text)

		if len(image_list) == 0:
			new_nodes.append(node)
		else:
			text_to_split = node.text

			for image in image_list:
				sections = text_to_split.split(f"![{image[0]}]({image[1]})", 1)
				if sections[0] != "":
					new_nodes.append(TextNode(sections[0], TextType.TEXT))
				new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
				text_to_split = sections[1]

			if text_to_split != "":
				new_nodes.append(TextNode(text_to_split, TextType.TEXT))
				
	return new_nodes

def split_nodes_links(old_nodes):
	new_nodes = []

	for node in old_nodes:
		links_list = extract_markdown_links(node.text)

		if len(links_list) == 0:
			new_nodes.append(node)
		else:
			text_to_split = node.text

			for link in links_list:
				sections = text_to_split.split(f"[{link[0]}]({link[1]})", 1)
				if sections[0] != "":
					new_nodes.append(TextNode(sections[0], TextType.TEXT))
				new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
				text_to_split = sections[1]

			if text_to_split != "":
				new_nodes.append(TextNode(text_to_split, TextType.TEXT))
				
	return new_nodes

def extract_markdown_images(text):
	# A markdown image has this format:  ![rick roll](https://i.imgur.com/aKaOqIh.gif)
	return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
	# A markdown link has this format:  [to boot dev](https://www.boot.dev)
	return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
