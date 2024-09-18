# if statements to test for different car names. Title case changes 
# appropriately

cars = ['audi', 'bmw', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'audi'