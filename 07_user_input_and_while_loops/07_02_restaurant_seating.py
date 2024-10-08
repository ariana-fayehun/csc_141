# I applied what I learned in the text to figure out how to complete this 
# assignment

# Asks for a number and converts it to an integer
group_number = input("How many people are in your dinner group? ")
group_number = int(group_number)

# Prints a message depending on how large the number is
if group_number >= 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")