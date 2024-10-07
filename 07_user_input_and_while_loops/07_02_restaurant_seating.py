group_number = input("How many people are in your dinner group? ")
group_number = int(group_number)

if group_number >= 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")