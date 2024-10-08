# I had to look back in the book to remember how to make while statements and
# inputs

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

