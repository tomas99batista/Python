# Example 4: Using command line arguments + exceptions

# Modify example3 to list every directory passed as argument.
# Report, but do not stop on errors with any argument.
# Execute as:
#   python3 example4.py dir1 dir2 etc...

import os
import sys

# (from example 3)
def listDirSizes(dname):
    lst = os.listdir(dname)
    for name in lst:
        # path = dir + "/" + name   	# not ideal...
        path = os.path.join(dname, name)	# this is better
        st = os.stat(path)		# get metadata about this path
        print(name, path, st.st_size)


# Using command line arguments
print("ARGV:", sys.argv)

for dname in sys.argv[1:]:
    try:
        print("---LISTING", dname)
        listDirSizes(dname)
        print("---END", dname)
    except FileNotFoundError:
        print("No found:", dname, file=sys.stderr)
    except NotADirectoryError:
        print("Not a directory:", dname, file=sys.stderr)    
    print()

