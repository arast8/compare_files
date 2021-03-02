# Author: Andrew Rast
# Date: 03/01/2021

import os
import filecmp

def compare_files(path_1, path_2):
	files_match = filecmp.cmp(path_1, path_2)

	if files_match:
		print("Files match.")
	else:
		print("Files do not match.")

def compare_dirs_differences(path_1, path_2):
	report = compare_dirs_differences_recurse(path_1, path_2).lstrip("\n")

	if report == "":
		print("Directories are identical.")
	else:
		print(report)

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

def compare_dirs_similarities(search_dir):
	"""
	Prints search_dir, then searches search_dir for duplicate files, printing
	the names of any duplicates.
	"""

	file_list = os.listdir(search_dir)
	total_duplicates = 0
	i = 0

	while i < len(file_list):
		file_i_name = file_list[i]
		file_i_path = os.path.join(search_dir, file_i_name)

		# only search the remaining portion of the list
		for j in range(i + 1, len(file_list)):
			file_j_name = file_list[j]
			file_j_path = os.path.join(search_dir, file_j_name)

			if filecmp.cmp(file_i_path, file_j_path):
				print("\t" + file_i_name + " = " + file_j_name)

				total_duplicates += 1

		i += 1

	if total_duplicates == 0:
		print("No duplicates.")

def compare_dirs_similarities(path_1, path_2):
	report = compare_dirs_similarities_recurse(path_1, path_2).lstrip("\n")

	if report == "":
		print("The directories have nothing in common.")
	else:
		print(report)

def compare_dirs_similarities_recurse(path_1, path_2):
	path_1_list = os.listdir(path_1)
	path_2_list = os.listdir(path_2)
	report = ""

	for item in path_1_list:
		item_1_path = os.path.join(path_1, item)
		item_2_path = os.path.join(path_2, item)

		if os.path.isfile(item_1_path) and os.path.isfile(item_2_path) and filecmp.cmp(item_1_path, item_2_path):
			report += "\n" + item_1_path + " = " + item_2_path
		elif os.path.isdir(item_1_path) and os.path.isdir(item_2_path):
			report += compare_dirs_similarities_recurse(item_1_path, item_2_path) # recurse

	return report
