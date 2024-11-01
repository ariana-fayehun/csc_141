# This class was moved from the other assignments in order to fill assignment 12


from user_module import User

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