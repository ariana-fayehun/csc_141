# 7 because it was hard to understand the previous code and make changes to it.

from pathlib import Path  # Import Path class from pathlib for easier file path handling
import json  # Import json module to work with JSON data format

def get_stored_user_info(path):
    """Get stored user information if available."""
    # Check if the file at the given path exists
    if path.exists():
        # If the file exists, read its contents
        contents = path.read_text()
        
        # Convert the JSON string in the file to a Python dictionary and return it
        return json.loads(contents)
    else:
        # If the file does not exist, return None
        return None

def greet_user():
    """Greet the user by name."""
    # Define the path to the JSON file where user information is stored
    path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/user_info.json')

    # Call the function to get stored user info from the file
    user_info = get_stored_user_info(path)

    # If user info exists (i.e., the file was found and parsed successfully)
    if user_info:
        # Retrieve the username from the stored user info dictionary (default to "User" if not found)
        username = user_info.get("username", "User")
        
        # Greet the user by their username
        print(f"Welcome back, {username}!")
        
        # Print the full user info stored in the file
        print("Here is your info: ")
        print(user_info)
    else:
        # If no user info is found, prompt the user for their information
        username = input("What is your name? ")
        age = input("What is your age? ")
        birth_month = input("What is your birth month? ")

        # Create a dictionary with the new user data
        user_info = {
            "username": username,
            "age": age,
            "birth_month": birth_month
        }

        # Convert the user_info dictionary to a JSON string
        contents = json.dumps(user_info)

        # Write the JSON string to the file to store the user info
        path.write_text(contents)
        
        # Confirm to the user that their info has been saved
        print(f"We'll remember you when you come back, {username}!")

# Call the greet_user function to run the program
greet_user()
