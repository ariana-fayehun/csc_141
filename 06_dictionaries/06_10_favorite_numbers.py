# I applied what I learned in the text to figure out how to complete this 
# assignment

# This dictionary connects a list of names with a number
favorite_numbers = {
    'nollan': ['3.14', '5'],
    'amos': ['6', '7'],
    'ariana': ['8', '6'],
    'athena': ['4', '2'],
    'rhea': ['5', '4'],
    }

# This prints the items in the dictionary in sentences based on the person's
# given number value
for name, numbers in favorite_numbers.items():
        print(f"\n{name.title()}'s favorite numbers are:")

        for number in numbers:
            print(f"\t{number.title()}")