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