import sys

# Check for the correct number of command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check if the file has a .py extension
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

# Try to open the file
try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()

except FileNotFoundError:
    sys.exit("File does not exist")

# Initialize the counter for lines of code
code_lines_count = 0

# Iterate over each line in the file
for line in lines:
    # Remove all leading and trailing whitespace
    stripped_line = line.strip()

    # Check if the line is not blank AND does not start with a comment
    if stripped_line and not stripped_line.startswith("#"):
        code_lines_count += 1

# 6. Print the final result
print(code_lines_count)
