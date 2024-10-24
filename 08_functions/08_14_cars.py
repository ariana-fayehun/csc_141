# I applied what I learned in the text to figure out how to complete this 
# assignment

def make_car(manufacturer, model, **other_info):
    """Provides info about a car and adds it to a dictionary"""
    other_info['manufacturer_name'] = manufacturer
    other_info['model_name'] = model
    return other_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)