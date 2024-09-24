# I followed the examples in the text to figure out how to complete this 
# assignment

# Defines a list of usernames
usernames = []

# Prints a message to every user but prints a specialized one if the user is
# an admin
# If there are no users, it prints a different message

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello, admin, would you like to see some status reports?")
        else:
            print(f"Hello, {username}! Welcome back.")
else:
    print("We need to find some users!")