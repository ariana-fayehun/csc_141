players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-2:])

print('Here are the first 3 players in the list')
for player in players[:3]:
    print(player.title())