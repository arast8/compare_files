# Author: Andrew Rast
# Date: 05/03/2021
#
# File and directory comparison algorithms

import os
import filecmp

def compare_files(path_1, path_2):
	files_match = filecmp.cmp(path_1, path_2)

	if files_match:
		return "Files match."
	else:
		return "Files do not match."

def compare_dirs_differences(path_1, path_2):
	report = compare_dirs_differences_recurse(path_1, path_2).lstrip("\n")

	if report == "":
		report = "Directories are identical."

	return report

def compare_dirs_differences_recurse(path_1, path_2):
	# dir_comp = filecmp.dircmp(path_1, path_2)

	# dir_comp.report_full_closure()

	path_1_list = os.listdir(path_1)
	path_2_list = os.listdir(path_2)

	only_in_1 = []
	only_in_2 = []
	items_in_both = []
	different_items = []
	report = ""

	for f in path_1_list:
		if f in path_2_list:
			items_in_both.append(f)
		else:
			report += "\nOnly in " + path_1 + ": " + f

	for f in path_2_list:
		if f not in path_1_list:
			report += "\nOnly in " + path_2 + ": " + f

	for f in items_in_both:
		item_1_path = os.path.join(path_1, f)
		item_2_path = os.path.join(path_2, f)

		if os.path.isdir(item_1_path) and os.path.isdir(item_2_path):
			report += compare_dirs_differences_recurse(item_1_path, item_2_path) # recurse
		elif os.path.isfile(item_1_path) and os.path.isfile(item_2_path):
			if not filecmp.cmp(item_1_path, item_2_path):
				report += "\nDifferent: " + item_1_path
		else:
			report += "\nFile vs. Directory: " + item_1_path

	return report

def compare_dir_duplicates(search_dir):
	"""
	Searches search_dir for duplicate files, including in subdirectories.
	"""
	file_list = get_file_list(search_dir)
	report = ""

	i = 0
	while i < len(file_list):
		file_i = file_list[i]

		# only search the remaining portion of the list
		for j in range(i + 1, len(file_list)):
			file_j = file_list[j]

			if filecmp.cmp(file_i, file_j):
				report += f"\n{file_i} = {file_j}"

		i += 1

	if report == "":
		report = "No duplicates."

	return report.lstrip("\n")

def compare_dirs_similarities(path_1, path_2):
	"""
	Finds identical files between path_1 and path_2, even if they don't have
	the same name.
	"""
	path_1_list = get_file_list(path_1)
	path_2_list = get_file_list(path_2)
	report = ""

	for file_1 in path_1_list:

		for file_2 in path_2_list:

			if filecmp.cmp(file_1, file_2):
				report += f"\n{file_1} = {file_2}"

	if report == "":
		report = "The directories have nothing in common."

	return report.lstrip("\n")

def get_file_list(directory):
	"""
	Walks the directory tree and returns a list of absolute paths to all files.
	"""
	file_list = []

	for root, dirs, files in os.walk(directory):
		for f in files:
			file_list.append(os.path.join(root, f))

	return file_list
