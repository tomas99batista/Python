# Example 1: Reading a file line-by-line

# Version 1: using readline in a while loop
"""
f = open("mystery.txt", "r")
while True:
    line = f.readline()
    if len(line)==0: break
    print(len(line), line)
f.close()
"""

# Version 2: using a for loop to iterate the lines in the file
"""
f = open("mystery.txt", "r")
for line in f:
    print(len(line), line)
f.close()
"""

# Version 3: Same thing, but using a with statement
with open("mystery.txt", "r") as f:
    print("Primeira", f.readline())
    for line in f:
        line = line.rstrip()
        print(len(line), line)

