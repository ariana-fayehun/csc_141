# I had to test some things in order to get it right. It kept printing the same
# thing over and over at first, but I fixed it

# Loop that asks for your age and prints a message accordingly
while True:
    age = input("What is your age? ")
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
        continue
    elif age < 12 and age >= 3:
        print("Your ticket is $10.")
        continue
    else:
        print("Your ticket is $15.")
        continue