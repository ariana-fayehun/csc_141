# I rate this assignment a 1 because the only thing I had to do different in
# this assignment was add line 11. I did struggle a bit because I forgot to
# store the replacement in the contents variable

# Imports Path from a library
from pathlib import Path

print("---This reads through the entire file---")
# Stores the path in a variable
path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/learning_python.txt')
contents = path.read_text() # Calls read_text on path and stores it in the var contents
contents = contents.replace('python', 'c++') # Replaces 'python' with 'c++'
print(contents) # Prints contents

print("\n---This splits the file into lines and prints each line---")
# Splits file into lines and stores it in lines
# lines = contents.splitlines() #Prints each line
for line in contents.splitlines():
    print(line)