# # name = input("Please enter your name: ")
# # print(f"Hello, {name}!")

# prompt = "If you share your name, we can personalize the message, you see."
# prompt += "\nWhat is yor first name? "

# name = input(prompt)
# print(f"Hello, {name}!")

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}")

greet_user('jesse')