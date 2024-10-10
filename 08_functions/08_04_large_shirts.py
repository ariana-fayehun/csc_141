# I applied what I learned in the text to figure out how to complete this 
# assignment

def make_shirt(message="I love Python!", size='large'):
    """Defines the size and message to be displayed on shirt"""
    print(f"The size of your shirt is {size} and the message that will be")
    print(f"displayed is '{message}'.")

# Uses both positional and keyword arguments to print two different statements
# about shirts
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='I love C++!')