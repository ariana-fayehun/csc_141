# I followed the examples in the text to figure out how to complete this 
# assignment

# defines a list of sandwich orders and an empty finished_sandwiches list
sandwich_orders = ['ham and cheese', 'pastrami', 'meatball', 'pastrami', 'pastrami', 'grilled cheese']
finished_sandwiches = []

# prints list of orders
print(sandwich_orders)

print("I'm sorry, but the restaurant has run our of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# while loop that pops sandwich from orders, prints message accordingly, and
# appends sandwich to finished sandwiches
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwhich.")
    finished_sandwiches.append(order)

# Prints sandwiches in finished sandwiches list
print("These were the sandwiches made:")
print(finished_sandwiches)