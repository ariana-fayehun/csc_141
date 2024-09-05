guest_list = ['Amos', 'Nollan', 'Ellie']

invite1 = f"Hello, {guest_list[0]}! You're invited to dinner!"
invite2 = f"Hello, {guest_list[1]}! You're invited to dinner!"
invite3 = f"Hello, {guest_list[2]}! You're invited to dinner!"


print(invite1)
print(invite2)
print(invite3)

print(f"Oh no! {guest_list.pop(1)} can't make it!")

guest_list.insert(1, 'Benson')
print(f"Instead, I'll invite {guest_list[1]} to dinner!")


print(invite1)
print(invite2)
print(invite3)

print("Attention, everyone! I have found a bigger table which means that I can invite more people.")


guest_list.insert(0, 'John')
guest_list.insert(-1, 'Athena')
guest_list.insert(2, 'Rhea')

invite1 = f"Hello, {guest_list[0]}! You're invited to dinner!"
invite2 = f"Hello, {guest_list[1]}! You're invited to dinner!"
invite3 = f"Hello, {guest_list[2]}! You're invited to dinner!"
invite4 = f"Hello, {guest_list[3]}! You're invited to dinner!"
invite5 = f"Hello, {guest_list[4]}! You're invited to dinner!"
invite6 = f"Hello, {guest_list[5]}! You're invited to dinner!"

print(invite1)
print(invite2)
print(invite3)
print(invite4)
print(invite5)
print(invite6)