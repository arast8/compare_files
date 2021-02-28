# Prompts the user for two file paths, compares the files' contents, and displays the differences, if any.

def main():
	repeat = "y"
	while repeat == "y" or repeat == "Y":
		file_a = open_file("A")
		file_b = open_file("B")
		if not isinstance(file_a, OSError) and not isinstance(file_b, OSError):
			lines_a = file_a.readlines()
			lines_b = file_b.readlines()
			min_length = 0

			if len(lines_a) >= len(lines_b):
				min_length = len(lines_a)
			else:
				min_length = len(lines_b)

			# Print differences in lines both files have
			for i in range(min_length):
				if lines_a[i] == lines_b[i]:
					print_difference(i, lines_a[i], lines_b[i])
			
			# Print remaining lines if one file has more
			if len(lines_a) > len(lines_b):
				for i in range(len(lines_b), len(lines_a)):
					print_difference(i, lines_a[i], "")
			elif len(lines_a) < len(lines_b):
				for i in range(len(lines_a), len(lines_b)):
					print_difference(i, "", lines_b[i])

			file_a.close()
			file_b.close()
		
		repeat = input("Repeat? (Y/n")

def open_file(name: str):
	"""Prompts user for file path and tries to open the file in read mode. Returns file object if successful or error if not.\n
	name - used to indicate to the user which file path to input"""
	path = input("File path " + name + ": ")
	try:
		return open(path, 'r')
	except OSError as identifier:
		#print("Error opening \"" + path + "\". File may not exist.", identifier)
		print(identifier)
		return identifier

def print_difference(i: int, a: str, b: str):
	""" i is the line number, a is the line from file a, and b is the line from file b"""
	print(str(i) + "A\t" + a)
	print(str(i) + "B\t" + b)


main()