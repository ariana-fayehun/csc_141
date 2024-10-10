# # # name = input("Please enter your name: ")
# # # print(f"Hello, {name}!")

# # prompt = "If you share your name, we can personalize the message, you see."
# # prompt += "\nWhat is yor first name? "

# # name = input(prompt)
# # print(f"Hello, {name}!")

# def greet_user(username):
#     """Display a simple greeting"""
#     print(f"Hello, {username.title()}")

# greet_user('jesse')

def get_formatted_name(first_name, last_name,middle_name=''):
    """Returns a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your full name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")