# I rate this assignment a 3 because I struggles to figure out how to add the
# names in a loop.

from pathlib import Path  # Import the Path class from the pathlib library for file handling

guest_list = ''  # Initialize an empty string to store guest names

# Infinite loop asking user to enter names until they enter 'q'
while True:
    name = input("What is your name? Enter 'q' to quit ")
    if name == 'q': 
        break
    elif guest_list == '':  # If guest list is empty, sets the string to the name
        guest_list = f"{name.title()}\n"
    else:
        guest_list += f"{name.title()}\n"  # If not empty, append the new name to the guest list with a newline

# Define the path where the guest book will be saved
path = Path("C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/guest_book.txt")
path.write_text(guest_list)  # Write the guest list to the specified file
