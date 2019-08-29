motorcycles = ['honda', 'yamaha', 'suzuki']

print (motorcycles)

motorcycles.append ('ducati')

print (motorcycles)

motorcycles.insert (0, 'bmw')

print (motorcycles)

del motorcycles[0]

print (motorcycles)

del motorcycles[1]

print (motorcycles)

last_owned = motorcycles.pop()

print ("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)

print ("The first motorcycle I owned was a " + first_owned.title() + ".")

print (motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'

print (motorcycles)

motorcycles.remove (too_expensive)

print (motorcycles)
print ("\nA " + too_expensive.title() + " is too expensive for me.")