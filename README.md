# compare_files

This is a Python app for comparing files and directories. compare_files.py is the command-line version, and ComparisonApp.py is the GUI version, which uses wxPython. Both versions use the same methods from comparison_algorithms.py to perform comparisons.

If two files are provided, it tells whether or not they are the same. If two directories are provided, it can list similarities or differences. If one directory is provided, it searches for duplicate files.

In the GUI version, the directory picker controls are drop targets, so you can drop files and directories onto them from a file manager.

Dependencies: [wxPython](https://wxpython.org/)
