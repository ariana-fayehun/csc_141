# I followed the examples in the text to figure out how to complete this assignment

from random import choice  # Import the choice function from the random module
number_picked = 0  # Initialize a variable to track the number of lottery numbers picked

# Define a list of possible lottery numbers (1-9, 0, and letters a-e)
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']
lottery_winner = []  # Initialize an empty list to store the winning lottery numbers

print("Any ticket that matches these four numbers or letters wins a prize!")  # Inform the user about the winning criteria

# Loop to randomly pick four numbers/letters for the lottery winner
while number_picked < 4:
    lottery_winner.append(choice(lottery))  # Randomly select a number/letter and add it to the lottery_winner list
    number_picked += 1  # Increment the count of numbers picked

print(lottery_winner)  # Print the list of winning lottery numbers/letters
