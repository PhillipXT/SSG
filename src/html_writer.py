import re, os

from src.markdown_html import markdown_to_html_node

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

	folders = dest_path.split("/")[:-1]
	current_folder = "./"
	for folder in folders:
		path = os.path.join(current_folder, folder)
		if not os.path.exists(path):
			os.mkdir(path)

	with open(dest_path, 'w') as file:
		file.write(file_content)

def extract_title(markdown):
	header = re.findall(r"^# .*", markdown)

	if header == []:
		raise Exception("No header found")
	
	return header[0][2:].strip()
