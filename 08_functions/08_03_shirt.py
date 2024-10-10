# I followed the examples in the text to figure out how to complete this 
# assignment

def make_shirt(size, message):
    """Defines the size and message to be displayed on shirt"""
    print(f"The size of your shirt is {size} and the message that will be")
    print(f"displayed is '{message}'.")

# Uses both positional and keyword arguments to print two different statements
# about shirts
make_shirt('5', 'Hello world!')
make_shirt(size='8', message='Coool Person!')