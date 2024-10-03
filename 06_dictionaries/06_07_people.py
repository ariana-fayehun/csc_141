# I followed the examples in the text to figure out how to complete this 
# assignment

# This code creates a dictionary defining some key characteristics about 
# someone
my_brother = {'first name': 'nollan', 'last name': 'fayehun', 'age': '15', 'city': 'aston'}
my_brother1 = {'first name': 'amos', 'last name': 'fayehun', 'age': '16', 'city': 'aston'}
me = {'first name': 'ariana', 'last name': 'fayehun', 'age': '18', 'city': 'reading'}

# creates a list out of the dictionaries
people = [my_brother, my_brother1, me]

# loops through the people in the list
for person in people:
    print(person)