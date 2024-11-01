# I needed to look back at the book to remember how to make a class
from restaurant_module import Restaurant

# class Restaurant:
#     """A class that models a restaurant"""

#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
    
#     def describe_restaurant(self):
#         print(f"{self.name} is a restaurant that serves {self.cuisine} food.")

#     def open_restaurant(self):
#         print(f"{self.name} is now open!")

# Defines restaurant1 and calls it using the class
restaurant1 = Restaurant("Hibachi", "Chinese")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()