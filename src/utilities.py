import os, shutil

def copy_folder(source, dest):

	if not os.path.exists(dest):
		print(f"Creating folder {dest}")
		os.mkdir(dest)

	for file in os.listdir(source):
		source_path = os.path.join(source, file)
		dest_path = os.path.join(dest, file)
		if os.path.isfile(source_path):
			print(f"Copying {source_path} to {dest_path}")
			shutil.copy(source_path, dest_path)
		else:
			copy_folder(source_path, dest_path)
