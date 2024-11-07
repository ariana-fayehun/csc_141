# 3 because I'm fairly comfortable with if-else statements at this point
# so it wasn't that hard to figure out.

from pathlib import Path  # Import Path class from pathlib to handle file paths easily
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
    
    # Get stored user info from the file by calling the get_stored_user_info function
    user_info = get_stored_user_info(path)

    # Check if user info was found (i.e., the file exists and contains valid data)
    if user_info:
        # Retrieve the username from the user_info dictionary, defaulting to "User" if not found
        username = user_info.get("username", "User")
        
        # Prompt the user to confirm if the username in the file is correct
        correct_user = input(f"Is {username} the correct user? (y/n) ")

    # If the user confirms that the username is correct
    if correct_user == 'y':
        # Print a welcome message using the stored username
        print(f"Welcome back, {username}!")
        
        # Print the full user info that was retrieved from the file
        print("Here is your info: ")
        print(user_info)
    else:
        # If the user indicated the username is not correct, prompt for new user information
        username = input("What is your name? ")
        age = input("What is your age? ")
        birth_month = input("What is your birth month? ")

        # Create a new dictionary with the updated user information
        user_info = {
            "username": username,
            "age": age,
            "birth_month": birth_month
        }

        # Convert the user_info dictionary to a JSON string
        contents = json.dumps(user_info)
        
        # Write the JSON string to the file to save the new user info
        path.write_text(contents)
        
        # Confirm to the user that their information has been saved
        print(f"We'll remember you when you come back, {username}!")

# Call the greet_user function to start the program
greet_user()
