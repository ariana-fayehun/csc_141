from city_functions import city_country

def test_city_country():
    """Does city_country work?"""
    formatted_city = city_country('santiago', 'chile')
    assert formatted_city == "santiago, chile"