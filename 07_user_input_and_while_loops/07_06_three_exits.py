# I edited 07_04 to include condtional statements, break statements, and active
# vars

# Version 1
# This version uses both a conditional statement and a break statement

# Defines the prompt
prompt = "Please enter a pizza topping:"
prompt += "\nEnter 'quit' to exit. "

# While loop that prints the topping entered or quits if user types 'quit'
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping}...")


# Version 2
# This version uses both a conditional statement and an active variable

# Defines the prompt
prompt = "Please enter a pizza topping:"
prompt += "\nEnter 'quit' to exit. "

active = True

# While loop that prints the topping entered or quits if user types 'quit'
while active:
    topping = input(prompt)

    if topping == 'quit':
        active == False
    else:
        print(f"Adding {topping}...")
