# I applied what I learned in the text to figure out how to complete this 
# assignment

# defines a dictionary of names and their favorite languages
favorite_languages = {
    'jen': 'python',
    'sara': 'c',
    'ed': 'rust',
    'phil': 'python',
    }

# defines a list of names of people who didn't take the poll
names = ['ariana', 'nollan', 'sara', 'ed']

# a loop that checks whether a name is in one of the keys of favorite languages
# and prints a message accordingly
for name in names:
    if name in favorite_languages.keys():
        print(f"Thank you for taking our poll, {name.title()}")
    else:
        print(f"Please take our poll, {name.title()}")

