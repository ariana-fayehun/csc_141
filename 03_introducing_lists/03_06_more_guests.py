guest_list = ['Amos', 'Nollan', 'Ellie']

print(f"Hello, {guest_list[0]}! You're invited to dinner!")
print(f"Hello, {guest_list[1]}! You're invited to dinner!")
print(f"Hello, {guest_list[2]}! You're invited to dinner!")

print(f"Oh no! {guest_list.pop(1)} can't make it!")

guest_list.insert(1, 'Benson')
print(f"Instead, I'll invite {guest_list[1]} to dinner!")

print(f"Hello, {guest_list[0]}! You're invited to dinner!")
print(f"Hello, {guest_list[1]}! You're invited to dinner!")
print(f"Hello, {guest_list[2]}! You're invited to dinner!")

print("Attention, everyone! I have found a bigger table which means that I can invite more people.")


guest_list.insert(0, 'John')
guest_list.insert(-1, 'Athena')
guest_list.insert(2, 'Rhea')

print(f"Hello, {guest_list[0]}! You're invited to dinner!")
print(f"Hello, {guest_list[1]}! You're invited to dinner!")
print(f"Hello, {guest_list[2]}! You're invited to dinner!")
print(f"Hello, {guest_list[3]}! You're invited to dinner!")
print(f"Hello, {guest_list[4]}! You're invited to dinner!")
print(f"Hello, {guest_list[5]}! You're invited to dinner!")