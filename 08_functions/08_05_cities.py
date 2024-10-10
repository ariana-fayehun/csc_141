# I followed the examples in the text to figure out how to complete this 
# assignment

def describe_city(name, country='america'):
    """Displays a message about a city/location"""
    print(f"{name.title()} is in {country.title()}")

# Prints city names and countries
describe_city(name='new york city')
describe_city(name='reading')
describe_city(name='ondo', country='africa')