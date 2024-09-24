# I applied what I learned in the text to figure out how to complete this 
# assignment

# This variable defines the variable 'pasta'
pasta = 'ramen'

# The following statements should all ask a question, then print the result 
# 'true'
print('Is pasta == "ramen"? I think it will be true.')
print(pasta == 'ramen')

print('Is pasta == "spaghetti" OR "ramen"? I think it will be true.')
print(pasta == 'spaghetti' or pasta == 'ramen')

print('Is "spaghetti" NOT IN pasta? I think it will be true.')
print('spaghetti' not in pasta)

print('Is "mac and cheese" NOT IN pasta? I think it will be true.')
print('mac and cheese' not in pasta)

print('Is "ramen" IN pasta? I think it will be true.')
print('ramen' in pasta)


# The following statements should all ask a question, then print the result 
# 'false'
print('Is pasta == "spaghetti"? I think it will be false.')
print(pasta == 'spaghetti')

print('Is pasta == "spaghetti" OR "mac and cheese"? I think it will be false.')
print(pasta == 'spaghetti' or pasta == 'mac and cheese')

print('Is pasta == "spaghetti" AND "ramen"? I think it will be false.')
print(pasta == 'spaghetti' and pasta == 'ramen')

print('Is "spaghetti" IN pasta? I think it will be false.')
print('spaghetti' in pasta)

print('Is "ramen" NOT IN pasta? I think it will be false.')
print('ramen' not in pasta)

# The following code defines the variable 'dog' and tests if it matches the
# value 'rhea'
dog = 'Rhea'

if dog.lower() == 'rhea':
    print(f'Hello {dog}!')

# The following code defines the variable 'favorite_number' and tests if it 
# matches different values
favorite_number = 8

if favorite_number == 8:
    print(f'My favorite number is {favorite_number}')

favorite_number = 9

if favorite_number != 8:
    print(f"{favorite_number}'s not my favorite number!")

if favorite_number > 8:
    print(f"Not {favorite_number}! Lower than that!")

if favorite_number >= 8:
    print(f"It could be {favorite_number}. But {favorite_number} could also be too big!")

favorite_number = 7

if favorite_number < 8:
    print(f"Not {favorite_number}! Higher than that!")

if favorite_number <= 8:
    print(f"It could be {favorite_number}. But {favorite_number} could also be too small!")