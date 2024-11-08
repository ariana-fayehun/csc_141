def city_country(city, country, population=''):
    "Formats city and country"
    if population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"