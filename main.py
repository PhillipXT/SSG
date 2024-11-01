from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode
from src.utilities import copy_folder

from src.markdown_text import extract_markdown_images, extract_markdown_links

def main():
	copy_folder("./static", "./public")

main()
