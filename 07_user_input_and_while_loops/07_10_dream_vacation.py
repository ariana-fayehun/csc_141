# I followed the examples in the text to figure out how to complete this 
# assignment

# Defines an empty dictionary for respsonses
responses = {}

# Flag that sets the poll to active
polling_active = True

# While loop that plays as long as polling_active is true.
# Asks for name and place, inputs answers into dictionary, and repeats loop
# if necessary
while polling_active:
    name = input("What is your name, user? ")
    place = input("If you could visit one place, where would you go? ")

    responses[name] = place
    
    repeat = input("Would you like to enter another resonse? (y/n) ")

    if repeat == 'n':
        break

# Prints results
print("\n=== Poll Results ===")
for name, place in responses.items():
    print(f"{name} would like to go to {place}")