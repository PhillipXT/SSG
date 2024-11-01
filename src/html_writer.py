import re, os

from pathlib import Path

from src.markdown_html import markdown_to_html_node

def generate_pages_recursive(content_path, template_path, dest_path):
	for file in os.listdir(content_path):
		new_source = os.path.join(content_path, file)
		new_dest = os.path.join(dest_path, file)
		if os.path.isfile(new_source):
			new_dest = Path(new_dest).with_suffix(".html")
			generate_page(new_source, template_path, new_dest)
		else:
			generate_pages_recursive(new_source, template_path, new_dest)

def generate_page(from_path, template_path, dest_path):
	print(f" * from {from_path} to {dest_path} using {template_path}")
	with open(from_path, 'r') as content_file:
		content = content_file.read()
	with open(template_path, 'r') as template_file:
		template = template_file.read()
	inner_html = markdown_to_html_node(content).to_html()
	title = extract_title(content)
	file_content = template.replace(r"{{ Title }}", title)
	file_content = file_content.replace(r"{{ Content }}", inner_html)

	dir_path = os.path.dirname(dest_path)
	if dir_path != "":
		os.makedirs(dir_path, exist_ok=True)

	with open(dest_path, 'w') as file:
		file.write(file_content)

def extract_title(markdown):
	header = re.findall(r"^# .*", markdown)

	if header == []:
		raise Exception("No header found")
	
	return header[0][2:].strip()
