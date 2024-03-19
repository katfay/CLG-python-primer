# slicing

pets = ['bird', 'cat', 'dog', 'canary', 'fish', 'horse']

pets[1] = 'lemur'
print(pets)

pets[1:3] = ['Duncan', 'dog2']

print(pets)

# adding: + (concatenation)

pets = ['ants', 'bird', 'cat', 'dog']
farm_animals = ['sheep', 'goat', 'cows']

animals = pets + farm_animals

print(animals)

# extend()
# function to add one list to another list; pass the additional list as a parameter

pets.extend(farm_animals)
print(pets)

# append()
# function to add an item to the end of a list

pets = ['ants', 'bird', 'cat', 'dog']
farm_animals = ['sheep', 'goat', 'cows']

pets.append('Duncan')
print(pets)

# insert()
# function to add an item to the middle of a list

pets = ['ants', 'bird', 'cat', 'dog']
farm_animals = ['sheep', 'goat', 'cows']

pets.insert(1, 'Duncan')
print(pets)

# remove()
# remove list elements

pets = ['ants', 'bird', 'cat', 'dog']

pets.remove('cat')
print(pets)
# prints: ['ants', 'bird', 'dog']


# pop()
# function to remove an element from a list and return it individually
pets = ['ants', 'bird', 'cat', 'dog']

pet = pets.pop()

print(pet)
print(pets)

# del
# function to delete one or multiple list items
pets = ['ants', 'bird', 'cat', 'dog']

del pets[2]
print(pets)

pets = ['ants', 'bird', 'cat', 'dog']
print(pets)

del pets[0:1]

print(pets)

pets = ['ants', 'bird', 'cat', 'dog']

del pets[0:3]

print(pets)
pets = ['ants', 'bird', 'cat', 'dog']

pets.remove('ants')
print(pets)

pets = ['ants', 'bird', 'cat', 'dog']
print(pets)
del pets[0]
print(pets)