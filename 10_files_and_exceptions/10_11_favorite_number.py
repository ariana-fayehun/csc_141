# 2 because I had to look back in the text to remember what to do.

from pathlib import Path  # Import Path class from pathlib for easy file path handling
import json  # Import json module to work with JSON data format

# Prompt the user to input their favorite number
favorite_number = input("What is your favorite number? ")

# Define the file path where the favorite number will be saved
path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/favorite_number.json')

# Convert the favorite number to a JSON string
contents = json.dumps(favorite_number)

# Write the JSON string to the specified file
path.write_text(contents)

# Confirm to the user that their favorite number has been saved
print("I'll remember that!")
