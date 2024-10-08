# I followed the examples in the text to figure out how to complete this 
# assignment

# Defines input statement asking foe a number
number = input("Please enter a number: ")

# Converts input into number
number = int(number)

# Prints statement depending on whether or not the number entered is a multiple
# of ten
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")