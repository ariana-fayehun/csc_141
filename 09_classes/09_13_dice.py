# I followed the examples in the text to figure out how to complete this 
# assignment

from random import randint  # Import the randint function from the random module
number_of_rolls = 0  # Initialize a variable to track the number of rolls

class Die:
    def __init__(self, sides=6):  # Initialize the Die class with a default of 6 sides
        self.sides = sides  # Set the number of sides for the die

    def roll_die(self):  # Define a method to roll the die
        print(randint(1, self.sides))  # Print a random number between 1 and the number of sides

# Create instances of Die with different numbers of sides
roll_die1 = Die()  # Create a 6-sided die
roll_die2 = Die(sides=10)  # Create a 10-sided die
roll_die3 = Die(sides=20)  # Create a 20-sided die

print("These are the numbers for the 6-sided die")  # Inform the user about the next output
while number_of_rolls < 10:  # Loop to roll the die 10 times
    roll_die1.roll_die()  # Roll the 6-sided die
    number_of_rolls += 1  # Increment the number of rolls

print("\nThese are the numbers for the 10-sided die")  # Inform the user about the next output

number_of_rolls = 0  # Reset the number of rolls for the next die

while number_of_rolls < 10:  # Loop to roll the die 10 times
    roll_die2.roll_die()  # Roll the 10-sided die
    number_of_rolls += 1  # Increment the number of rolls

print("\nThese are the numbers for the 20-sided die")  # Inform the user about the next output

number_of_rolls = 0  # Reset the number of rolls for the next die

while number_of_rolls < 10:  # Loop to roll the die 10 times
    roll_die3.roll_die()  # Roll the 20-sided die
    number_of_rolls += 1  # Increment the number of rolls
