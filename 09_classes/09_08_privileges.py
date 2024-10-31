# I applied what I learned in the text to figure out how to complete this 
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


class Privileges:
    """A class to represent the privileges associated with an Admin user."""

    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        # Initialize the Privileges class with a default list of privileges
        self.privileges = privileges  # Store the list of privileges

    def show_privileges(self):
        """Display the privileges of the Admin user."""
        print("Here is an admin's privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Defines an Admin user, a specific type of User with special privileges."""

    def __init__(self, first_name, last_name, age, place):
        # Initialize the User parent class with general user information
        super().__init__(first_name, last_name, age, place)
        # Initialize the Privileges instance for Admin, containing a list of privileges
        self.privileges = Privileges()  # Assign a Privileges instance to the Admin

# Create an Admin instance with specific name, age, and place information
admin1 = Admin('aria', 'fay', 18, 'reading')
# Call the describe_user method to display personal information of the admin
admin1.describe_user()
# Display the admin's privileges by calling the show_privileges method of Privileges
admin1.privileges.show_privileges()
