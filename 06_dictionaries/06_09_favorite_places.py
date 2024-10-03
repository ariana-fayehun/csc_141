# I followed the examples in the text to figure out how to complete this 
# assignment

# defines a dictionary with keys that are names and values that are places
favorite_places = {
    'ariana': ['japan', 'south korea'],
    'nollan': ['japan', 'china'],
    'amos': ['london']
}

# loops through names and places and prints a message depending on how many
# favorite places a person has
for name, places in favorite_places.items():
    if len(places) >= 2:

        print(f"\n{name.title()}'s favorite places are:")

        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favorite place is:")
        print(place.title())