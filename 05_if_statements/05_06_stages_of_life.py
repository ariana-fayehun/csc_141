# I applied what I learned in the text to figure out how to complete this 
# assignment

# Defines age
age = 18

# Prints a specialized message depending on how big the variable 'age' is
if age < 2:
    print("You are a baby.")
elif (age >= 2) and (age < 4):
    print("You are a toddler.")
elif (age >= 4) and (age < 13):
    print("You are a kid.")
elif (age >= 13) and (age < 20):
    print("You are a teen.")
elif (age >= 20) and (age < 65):
    print("You are a adult.")
else:
    print("You are an elder.")