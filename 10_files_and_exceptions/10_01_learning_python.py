# I rate this assignment a 3 because I had trouble remembering what to do and
# had to look back in the text.

# Imports Path from a library
from pathlib import Path

print("---This reads through the entire file---")
# Stores the path in a variable
path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/learning_python.txt')
contents = path.read_text() # Calls read_text on path and stores it in the var contents
print(contents) # Prints contents

print("\n---This splits the file into lines and prints each line---")
# Splits file into lines and stores it in lines
# lines = contents.splitlines() #Prints each line
for line in contents.splitlines():
    print(line)