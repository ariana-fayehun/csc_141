# requested_toppings = ['mushrooms', 'peperoni', 'extra cheese', 'green peppers']

# # if requested_topping != 'anchovies':
# #     print('Hold the anchovies!')

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print(f"Sorry, we are out of {requested_topping}.")
#     else:
#         print(f"Adding {requested_topping}...")
    
# print("Your pizza is done!")

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}...")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'peperoni', 'extra cheese', 'green peppers']

requested_toppings = ['noodles', 'peperoni', 'tomatoes', 'green peppers']

added_toppings = []

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}...")
        added_toppings.append(requested_topping)
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("Finished making your pizza!")
print("Here are the toppings that were added:")
print(added_toppings)