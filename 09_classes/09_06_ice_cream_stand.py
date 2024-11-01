# I applied what I learned in the text to figure out how to complete this 
# assignment
from restaurant_module import Restaurant

# class Restaurant:
#     """A class that models a restaurant"""

#     def __init__(self, name, cuisine):
#         # Initialize the restaurant with a name and type of cuisine
#         self.name = name  # Name of the restaurant
#         self.cuisine = cuisine  # Type of cuisine served by the restaurant
    
#     def describe_restaurant(self):
#         # Display a description of the restaurant
#         print(f"{self.name} is a restaurant that serves {self.cuisine} food.")

#     def open_restaurant(self):
#         # Indicate that the restaurant is open
#         print(f"{self.name} is now open!")


class IceCreamStand(Restaurant):
    """Models an ice cream stand, a specific type of restaurant"""
    
    def __init__(self, name, cuisine):
        # Initialize attributes from the parent class (Restaurant)
        super().__init__(name, cuisine)
        # Add a list of ice cream flavors specific to the ice cream stand
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def IceCreamFlavors(self):
        # Display the list of available ice cream flavors
        print("The flavors are:")
        print(self.flavors)

# Create an instance of IceCreamStand named 'brusters'
brusters = IceCreamStand('brusters', 'ice cream')
# Call describe_restaurant method to display information about the ice cream stand
brusters.describe_restaurant()
# Call IceCreamFlavors method to list the flavors available at the ice cream stand
brusters.IceCreamFlavors()
