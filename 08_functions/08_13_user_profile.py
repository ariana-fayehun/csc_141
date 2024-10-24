# I followed the examples in the text to figure out how to complete this 
# assignment

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('ariana', 'fayehun', location='reading',
                             major='game and sim', enjoys='drawing')

print(user_profile)