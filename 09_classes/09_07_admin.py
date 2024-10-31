# I followed the examples in the text to figure out how to complete this 
# assignment

class User:
    """Defines a class for a user with attributes and methods for describing and greeting them."""

    def __init__(self, first_name, last_name, age, place):
        """Initialize the User class with personal information."""
        self.first = first_name  # Store the user's first name
        self.last = last_name    # Store the user's last name
        self.age = age           # Store the user's age
        self.place = place       # Store the user's place of residence or origin

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nFirst name: {self.first}")
        print(f"Last name: {self.last}")
        print(f"Age: {self.age}")
        print(f"Place: {self.place}")

    def greet_user(self):
        """Print a greeting to the user."""
        print(f"Hello, {self.first} {self.last}!")

class Admin(User):
    """Defines a class for an admin user, which is a specific type of User."""
    
    def __init__(self, first_name, last_name, age, place):
        # Initialize the parent class (User) with common user attributes
        super().__init__(first_name, last_name, age, place)
        # Add a list of privileges unique to the Admin class
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Print a list of the admin's privileges."""
        print("Here is an admin's privileges:")
        print(self.privileges)

# Create an instance of the Admin class with name, age, and place information
admin1 = Admin('aria', 'fay', 18, 'reading')
# Call the describe_user method to display the admin's personal information
admin1.describe_user()
# Call the show_privileges method to display the admin's privileges
admin1.show_privileges()
