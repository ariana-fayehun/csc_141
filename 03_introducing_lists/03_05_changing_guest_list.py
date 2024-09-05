guest_list = ['Amos', 'Nollan', 'Ellie']

invite1 = f"Hello, {guest_list[0]}! You're invited to dinner!"
invite2 = f"Hello, {guest_list[1]}! You're invited to dinner!"
invite3 = f"Hello, {guest_list[-1]}! You're invited to dinner!"

print(invite1)
print(invite2)
print(invite3)

print(f"Oh no! {guest_list.pop(1)} can't make it!")

guest_list.insert(1, 'Benson')
print(f"Instead, I'll invite {guest_list[1]} to dinner!")


print(invite1)
print(invite2)
print(invite3)