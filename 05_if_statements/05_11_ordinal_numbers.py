# I followed the examples in the text to figure out how to complete this 
# assignment

# Defines a list of numbers
numbers = ['1','2','3','4','5','6','7','8','9']

# Prints a different ending depending on what number it is.
for number in numbers:
    if number == '1':
        print(f"{number}st")
    elif number == '2':
        print(f"{number}nd")
    elif number == '3':
        print(f"{number}rd")
    else:
        print(f"{number}th")