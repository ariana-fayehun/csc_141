# I applied what I learned in the text to figure out how to complete this 
# assignment

def make_sandwhich(*ingredients):
    """Prints the ingredients that will be put into the sandwhich"""
    print("\nMaking a sandwhich with the following ingredients:")
    for ingredient in ingredients:
        print(f" - {ingredient}")

make_sandwhich('ham')
make_sandwhich('ham', 'cheese')
make_sandwhich('lettuce', 'tomatoes', 'cheese')