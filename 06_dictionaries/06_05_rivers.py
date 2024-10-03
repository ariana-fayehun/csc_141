# I followed the examples in the text to figure out how to complete this 
# assignment

# defines a dictionary of rivers and locations
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'mississippi': 'usa'}

# loops through the rivers and places and puts them in a sentence
for river, place in rivers.items():
    if place == 'usa':
        print(f"The {river.title()} River is in {place.upper()}")
    else:
        print(f"The {river.title()} River is in {place.title()}")

# loops through the rivers
for river in rivers.keys():
    print(river.title())

# loops through the places
for place in rivers.values():
    print(place.title())