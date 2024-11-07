# 1 because it was easy to turn it into an if-else statement

from pathlib import Path  # Import Path class from pathlib to handle file paths
import json  # Import json module to work with JSON data format

# Define the file path to store or read the favorite number
path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/favorite_number.json')

# Check if the file already exists to see if the favorite number is stored
if path.exists():
    # If the file exists, read the contents
    contents = path.read_text()

    # Parse the JSON data from the file to retrieve the favorite number
    number = json.loads(contents)

    # Print the user's stored favorite number
    print(f"Your favorite number is {number}")
else:
    # If the file doesn't exist, prompt the user to input their favorite number
    favorite_number = input("What is your favorite number? ")

    # Convert the input to a JSON string format
    contents = json.dumps(favorite_number)

    # Write the JSON string to the file to save the favorite number
    path.write_text(contents)

    # Confirm to the user that their favorite number has been saved
    print("I'll remember that!")
