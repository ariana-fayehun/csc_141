# I rate this assignment a 2 because I had to look back in the textbook but
# there wasn't that much I needed to do for this one

# Imports Path
from pathlib import Path

# Asks user for name
name = input("What is your name? ")

path = Path("C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/guest.txt")
print("Your name has been added to guest.txt")

# Creates text file and prints this message inside
path.write_text(f"Hello {name.title()}!")