# I needed to look back at the book to remember how to make a class

# Define the 'Restaurant' class to model a restaurant's basic attributes and behaviors
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

# Create an instance of the 'Restaurant' class named restaurant1
restaurant1 = Restaurant("Hibachi", "Chinese")

# Call the describe_restaurant method to print details about the restaurant
restaurant1.describe_restaurant()

# Call the open_restaurant method to announce that the restaurant is open
restaurant1.open_restaurant()

# Call the served method to display the initial number of customers served (0)
restaurant1.served()

# Manually set the number of people served to 500 and display it
restaurant1.number_served = 500
restaurant1.served()

# Use the set_number_served method to change the number served to 620 and display it
restaurant1.set_number_served(620)
restaurant1.served()

# Use the increment_number_served method to increase the number served by 100
restaurant1.increment_number_served(100)
restaurant1.served()
