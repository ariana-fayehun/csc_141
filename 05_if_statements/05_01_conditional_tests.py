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