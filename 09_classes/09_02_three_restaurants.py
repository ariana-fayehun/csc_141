# I needed to look back at the book to remember how to make a class

class Restaurant:
    """A class that models a restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"{self.name} is a restaurant that serves {self.cuisine} food.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

# Defines restaurant1, 2, and 3 and calls them using the class
restaurant1 = Restaurant("Hibachi", "Chinese")
restaurant2 = Restaurant("Panda Express", "Chinese")
restaurant3 = Restaurant("McDonalds", "Fast Food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
