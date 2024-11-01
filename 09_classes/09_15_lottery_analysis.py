# I followed the examples in the text to figure out how to complete this assignment

from random import choice  # Import the choice function from the random module
number_picked = 0  # Initialize a variable to track the number of lottery numbers picked
number_of_tries = 0  # Initialize a variable to count the number of tries to find a winning ticket

# Define a list of possible lottery numbers (1-9, 0, and letters a-e)
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']
lottery_winner = []  # Initialize an empty list to store the winning lottery numbers
my_ticket = []  # Initialize an empty list to store the user's lottery ticket

print("Any ticket that matches these four numbers or letters wins a prize!")  # Inform the user about the winning criteria

# Loop to randomly pick four numbers/letters for the lottery winner
while number_picked < 4:
    lottery_winner.append(choice(lottery))  # Randomly select a number/letter and add it to the lottery_winner list
    number_picked += 1  # Increment the count of numbers picked

print(lottery_winner)  # Print the list of winning lottery numbers/letters

# Loop to keep generating a ticket until it matches the winning numbers
while my_ticket != lottery_winner:
    number_picked = 0  # Reset the number of picked numbers for the new ticket
    number_of_tries += 1  # Increment the try counter
    my_ticket.clear()  # Clear the previous ticket numbers

    # Loop to randomly pick four numbers/letters for the user's ticket
    while number_picked < 4:
        my_ticket.append(choice(lottery))  # Randomly select a number/letter and add it to my_ticket
        number_picked += 1  # Increment the count of numbers picked

# Print the total number of tries taken to match the winning ticket
print(f"It took me {number_of_tries} to get the winning ticket!")
