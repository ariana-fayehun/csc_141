from city_functions_population import city_country

def test_city_country():
    """Does city_country work?"""
    formatted_city = city_country('santiago', 'chile')
    assert formatted_city == "santiago, chile"

def test_city_country_population():
    """Does city_country work?"""
    formatted_city = city_country('santiago', 'chile', population=500000)
    assert formatted_city == "santiago, chile - population 500000"