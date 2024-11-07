# 1 because I forgot how to encode, but the rest was easy.

from pathlib import Path  # Import Path class from pathlib module to work with file paths

# Define the file path to the text file
path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/gutenberg.txt')

# Read the contents of the file, specifying 'utf-8' encoding for proper character interpretation
contents = path.read_text(encoding='utf-8')

# Convert the contents to lowercase and count occurrences of the word 'the ' (with a space after 'the')
print(contents.lower().count('the '))
