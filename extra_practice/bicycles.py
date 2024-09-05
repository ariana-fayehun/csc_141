bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())
print(bicycles[3].title())
print(bicycles[-2].title())

message  = f"My first bicycle was a {bicycles[0].title()}"
print(message)

bicycles[0] = 'nothing'

print(bicycles[0])
print(bicycles)

bicycles.append('ducati')
print(bicycles)

motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'nothing')

print(motorcycles)

del motorcycles[3]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)