#I followed the examples in the text to figure out how to complete this 
# assignment
from user_module import User

# class User:
#     """Defines a class for a user with attributes and methods for describing and greeting them."""

#     def __init__(self, first_name, last_name, age, place):
#         """Defines the User class with personal information."""
#         self.first = first_name  # Store the first name
#         self.last = last_name    # Store the last name
#         self.age = age           # Store the age
#         self.place = place       # Store the place of residence or origin

#     def describe_user(self):
#         """Prints a summary of the user's information."""
#         print(f"\nFirst name: {self.first}")
#         print(f"Last name: {self.last}")
#         print(f"Age: {self.age}")
#         print(f"Place: {self.place}")

#     def greet_user(self):
#         """Prints a greeting to the user."""
#         print(f"Hello, {self.first} {self.last}!")


# Create three instances of the User class with different personal data
user1 = User("Aria", "Fay", 18, "Reading")
user2 = User("Luna", "Moon", 16, "Moss Deep")
user3 = User("Rhea", "Sunshine", 18, "Penn")

# Call methods on each user instance to display their details and greet them
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
