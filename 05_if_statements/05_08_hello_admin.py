# I applied what I learned in the text to figure out how to complete this 
# assignment

# Defines a list of usernames
usernames = ['admin','user1','hiimuser','userisme12','cooluser101']

# Prints a message to every user but prints a specialized one if the user is
# an admin
for username in usernames:
    if username == 'admin':
        print("Hello, admin, would you like to see some status reports?")
    else:
        print(f"Hello, {username}! Welcome back.")