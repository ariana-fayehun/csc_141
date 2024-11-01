# This class was moved from the other assignments in order to fill assignment 10

class Restaurant:
    """A class that models a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize attributes: restaurant's name, cuisine type, and people served."""
        self.name = name  # Store the name of the restaurant
        self.cuisine = cuisine  # Store the type of cuisine served
        self.number_served = 0  # Initialize the number of customers served to 0
    
    def describe_restaurant(self):
        """Print a description of the restaurant's name and cuisine type."""
        print(f"{self.name} is a restaurant that serves {self.cuisine} food.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.name} is now open!")

    def served(self):
        """Print the number of people the restaurant has served."""
        print(f"{self.name} has served {self.number_served} people!")

    def set_number_served(self, number):
        """Set the number of customers served to a given value."""
        self.number_served = number  # Update the number of customers served

    def increment_number_served(self, number):
        """Increase the number of customers served by a specified amount."""
        self.number_served += number  # Add to the current number of customers served