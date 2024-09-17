my_foods = ['ramen', 'spaghetti', 'white rice', 'jollof rice']
brothers_foods = my_foods[:]

my_foods.append('mexican rice')
brothers_foods.append('pounded yam')

print(f'My favorite foods are:')
for my_food in my_foods:
    print(my_food)

print(f"My brother's favorite foods are:")
for brothers_food in brothers_foods:
    print(brothers_food)