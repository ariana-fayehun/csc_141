# I edited many_users.py by adding more users

# defines a dictionary of users and info about them
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'enstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    'rsunshine': {
        'first': 'rhea',
        'last': 'sunshine',
        'location': 'usa',
        },

    'amoon': {
        'first': 'amethyst',
        'last': 'moon',
        'location': 'internet',
        },
}

# a loop that prints each user and info about them
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"Full name: {full_name.title()}")
    print(f"Location: {location.title()}")