# 2 because I had to look back in the text to remember what to do.

from pathlib import Path  # Import Path class from pathlib for file path handling
import json  # Import json module to work with JSON data

# Define the file path to the JSON file containing the favorite number
path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/favorite_number.json')

# Read the contents of the file as a string
contents = path.read_text()

# Retrieves the stored favorite number
number = json.loads(contents)

# Print the user's favorite number
print(f"Your favorite number is {number}")
