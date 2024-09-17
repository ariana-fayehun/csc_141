pizzas = ['peperoni', 'meatlovers', 'vegetable']

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I don't really like pizza...")

friend_pizzas = pizzas[:]
pizzas.append('cheese')
friend_pizzas.append('hawaiian')

print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print(f"My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)