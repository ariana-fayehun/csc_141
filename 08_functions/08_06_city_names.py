# I applied what I learned in the text to figure out how to complete this 
# assignment

def city_country(name, country):
    """Displays a city and its country"""
    name_location = f"{name}, {country}"
    return name_location.title()

# Prints cities and countries
print(city_country('new york city', 'united states of america'))
print(city_country('philadelphia', 'united states of america'))
print(city_country('ondo', 'africa'))