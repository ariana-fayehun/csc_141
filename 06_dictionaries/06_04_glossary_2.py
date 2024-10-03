# I had to look back in the book to remember how to loop through a dictionary
# Afterward, I added five new terms


# This dictionary defines a list of terms by listing the term, followed by
# the definition
glossary = {
    'dictionary': 'a collection of valur pairs that allow you to access/store data',
    'if statement': 'used to execute code if a statement is true',
    'variable': 'used to store a value',
    'string': 'a statement enclosed in quotes to create text',
    'float': 'a data type used to represent numbers',
    'for loop': 'repeats a set of actions for each item in a list or group of things',
    'print': 'used to display text or other information to the screen',
    'integer': 'a whole number',
    'elif block': ' used to check another condition if the previous if statement is not true',
    'else block': 'used to specify a block of code that runs if none of the previous if or elif conditions are met',
    }

# The following loop simplifies the original print statements yet still prints
# each term and definition
print("Glossary:")
for term, definition in glossary.items():
    print(f"\n{term}: {definition}")




# print("Glossary\n")
# print(f"Dictionary: {glossary['dictionary']}\n")
# print(f"If Statement: {glossary['if statement']}\n")
# print(f"Variable: {glossary['variable']}\n")
# print(f"String: {glossary['string']}\n")
# print(f"Float: {glossary['float']}\n")