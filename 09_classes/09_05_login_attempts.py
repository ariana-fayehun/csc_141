# I followed the examples in the text to figure out how to complete this assignment
from user_module import User

# Define the User class, modeling a user with personal information and login tracking
# class User:
#     """Defines a class for a user with attributes and methods for describing and greeting them."""

#     def __init__(self, first_name, last_name, age, place):
#         """Initialize the user's attributes: name, age, place, and login attempts."""
#         self.first = first_name  # Store the user's first name
#         self.last = last_name    # Store the user's last name
#         self.age = age           # Store the user's age
#         self.place = place       # Store the user's place of residence or origin
#         self.login_attempts = 0  # Initialize login attempts to 0

#     def describe_user(self):
#         """Prints a summary of the user's information."""
#         print(f"\nFirst name: {self.first}")  # Display first name
#         print(f"Last name: {self.last}")      # Display last name
#         print(f"Age: {self.age}")             # Display age
#         print(f"Place: {self.place}")         # Display place of residence

#     def greet_user(self):
#         """Prints a personalized greeting for the user."""
#         print(f"Hello, {self.first} {self.last}!")  # Greet the user by name

#     def increment_login_attempts(self):
#         """Increases the login attempt count by one."""
#         self.login_attempts += 1  # Add 1 to the current login attempts

#     def reset_login_attempts(self):
#         """Resets the login attempt count to zero."""
#         self.login_attempts = 0  # Set the login attempts back to 0


# Create an instance of the User class with specific personal details
user1 = User("Aria", "Fay", 18, "Reading")  

# Simulate multiple login attempts by calling increment_login_attempts() four times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print the current number of login attempts (should be 4)
print(user1.login_attempts)  # Output: 4

# Reset the login attempts to 0
user1.reset_login_attempts()

# Print the number of login attempts again (should be 0 after reset)
print(user1.login_attempts)  # Output: 0
