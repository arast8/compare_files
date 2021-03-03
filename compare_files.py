# Author: Andrew Rast
# Date: 03/01/2021
#
# Command line tool for comparing files or directories.

from comparison_algorithms import *

def main():
	print("Compares files or directories")

	again = True
	path_1 = ""
	path_2 = ""
	operation_type = 0
	input_is_valid = False

	while(again):
		print()
		
		path_1 = input("Enter path 1: ")
		while not os.path.exists(path_1):
			path_1 = input("Invalid path. Enter path 1: ")

		path_2 = input("Enter path 2: ")
		while path_2 != "" and not os.path.exists(path_2):
			path_2 = input("Invalid path. Enter path 2: ")

		while not input_is_valid:
			input_string = input("Find similarities (1) or differences (2)?: ")
			
			try:
				operation_type = int(input_string)

				if operation_type == 1 or operation_type == 2:
					input_is_valid = True
			except:
				pass
			
			if not input_is_valid:
				print("Invalid input. ", end="")
		input_is_valid = False

		if os.path.isfile(path_1) and os.path.isfile(path_2):
			if operation_type == 2:
				print(compare_files(path_1, path_2))
			else:
				print("Invalid operation.")
		elif os.path.isdir(path_1) and os.path.isdir(path_2):
			if operation_type == 1:
				print(compare_dirs_similarities(path_1, path_2))
			elif operation_type == 2:
				print(compare_dirs_differences(path_1, path_2))
			else:
				print("Invalid operation.")
		elif os.path.isdir(path_1) and path_2 == "":
			print(compare_dir_duplicates(path_1))
		else:
			print("Can't compare file and directory.")

		choice = input("Compare more files? (Y/n): ").lower()

		again = choice == "y" or choice == "yes"

main()
