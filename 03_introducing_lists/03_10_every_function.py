pasta = ['ramen', 'spaghetti', 'lo mein', 'lasagna']

print(f"I like {pasta[0]} the most.")

print(f"I don't like {pasta.pop(-1)} very much, so I'll remove it.")

pasta.insert(3, 'macaroni')
print(f"Instead, I'll add {pasta[3]}.")

del pasta[2]

print(sorted(pasta))

print(pasta)

print(sorted(pasta, reverse=True))

print(pasta)

pasta.reverse()
print(pasta)

pasta.reverse()
print(pasta)

pasta.sort()
print(pasta)

pasta.sort(reverse=True)
print(pasta)

print(f"There are {len(pasta)} pasta on the list.")