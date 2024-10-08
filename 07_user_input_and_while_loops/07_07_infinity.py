# I edited 07_05 because I accidentally made an infinite loop in that one before
# fixing it

# Var that gets your age
age = input("What is your age? ")
age = int(age)

# Infinite while loop that prints ticket price if your age is greater than or
# equal to 0
while True:
    if age >= 0:
        print("Your ticket is free!")
        continue