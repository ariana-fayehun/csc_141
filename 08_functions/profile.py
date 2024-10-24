# This file serves as a module for assignment 08_15


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info