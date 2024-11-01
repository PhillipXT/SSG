import os, shutil

def copy_folder(source, dest):

	if not os.path.exists(source):
		raise Exception("Source directory does not exist.")
	
	if not os.path.exists(dest):
		raise Exception("Destination directory does not exist.")

	print(f"Deleting {dest}")
	shutil.rmtree(dest, ignore_errors=True)

	files = get_file_list(source)

	for file in files:
		source_path = file[0]
		source_file = source_path + "/" + file[1]
		dest_path = source_path.replace(source, dest)
		print(f"Moving {source_file} to {dest_path}")
		if not os.path.exists(dest_path):
			os.mkdir(dest_path)
		shutil.copy(source_file, dest_path)

def get_file_list(source):

	structure = []

	files = os.listdir(source)

	if files == []:
		return []
	
	for file in files:
		if os.path.isdir(source + "/" + file):
			path = source + "/" + file
			structure.extend(get_file_list(path))
		else:
			structure.append((source, file))

	return structure
