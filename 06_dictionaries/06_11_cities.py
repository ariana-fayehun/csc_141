# I followed the examples in the text to figure out how to complete this 
# assignment

# a dictionary with dictionaries inside that define a city and some facts about
# it
cities = {
    'nyc': {
        'country': 'usa',
        'population': '8.336 million',
        'fact': 'This city never sleeps',
        },

    'philadelphia': {
        'country': 'usa',
        'population': '1.567 million',
        'fact': 'Houses the liberty bell',
        },

    'reading': {
        'country': 'usa',
        'population': '94,858',
        'fact': 'Is one of the poorest cities in the US',
        },
    }

# prints each city and its values
for city, values in cities.items():
    print(f"{city}: {values}")