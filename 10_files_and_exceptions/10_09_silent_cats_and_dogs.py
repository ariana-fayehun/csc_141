# I rate this assignment a 0 because I only had to change the "except" block to
# "pass"

from pathlib import Path  # Import the Path class from the pathlib module to handle file paths

# Define the file path for the 'cats.txt' file using an absolute path.
path1 = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/cats.txt')

# Define the file path for the 'dogs.txt' file using a relative path that does not work.
path2 = Path('dogs.txt')

# Attempt to read and print the contents of the 'cats.txt' file.
try:
    contents1 = path1.read_text()  # Read the text from path1 if the file exists
    print(contents1)  # Print the contents of 'cats.txt'
except FileNotFoundError:
    # Handle the error if 'cats.txt' is not found
    pass

# Attempt to read and print the contents of the 'dogs.txt' file.
try:
    contents2 = path2.read_text()  # Read the text from path2 if the file exists
    print(contents2)  # Print the contents of 'dogs.txt'
except FileNotFoundError:
    # Handle the error if 'dogs.txt' is not found
    pass
