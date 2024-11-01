import os, shutil

from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode
from src.utilities import copy_folder
from src.html_writer import generate_page

from src.markdown_text import extract_markdown_images, extract_markdown_links

def main():

	dir_path_static = "./static"
	dir_path_public = "./public"
	dir_path_content = "./content"

	print(f"Current directory: {os.getcwd()}")

	print(f"Deleting {dir_path_public}")
	if os.path.exists(dir_path_public):
		shutil.rmtree(dir_path_public)

	print("Copying static files to public directory...")
	copy_folder(dir_path_static, dir_path_public)

	print(f"Generating pages:")
	generate_page(os.path.join(dir_path_content, 'index.md'), 'template.html', os.path.join(dir_path_public, 'index.html'))

main()
