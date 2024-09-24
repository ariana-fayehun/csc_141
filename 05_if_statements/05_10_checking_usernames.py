# I applied what I learned in the text to figure out how to complete this 
# assignment. It took some trial and error to remember how to convers strings
# in a list into lowercase.

# These variables define the current users, an empty list of lowercase
# users, and the new users.
current_users = ['COOLadmin','user1','hiimuser','userisme12','cooluser101']
current_users_lower = []
new_users = ['cooladmin','james','jesse','meowth','cooluser101']


# This for loop converts the strings in 'current_users' to lowercase and appends
# it to 'current_users_lower'
for current_user in current_users:
    current_users_lower.append(current_user.lower())

# This for loop checks if a new user is in the list of lowercase current users
# and prints a message depending on whether or not the result is True.
for new_user in new_users:
    if new_user in current_users_lower:
        print("That username is taken. Please choose another.")
    else:
        print("That username is avaible.")