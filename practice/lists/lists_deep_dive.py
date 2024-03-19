# sort()
# reverse()
# len()
# count()

# sort() 
# sort list of numbers in asc numerical order; sort list of strings in alpha order 

numbers = [12, 3, -3, -3.45, 0, 192]
print(numbers)
numbers.sort()
print(numbers)

pets = ["Duncan", "Chessie", "Eric", "fish"]
print(pets)
pets.sort()
print(pets)

 # reverse sort a list of numbers or str from its existing state 
numbers = [12, 3, -3, -3.45, 0, 192]
print(numbers)
numbers.reverse()
print(numbers)

pets = ["Duncan", "Chessie", "Eric", "fish"]
print(pets)
pets.reverse()
print(pets)

# len()
# get the length of a list (number of elements in the list) by passing the list as an argument

pets = ["Duncan", "Chessie", "Eric", "fish"]

print(len(pets))

# count()
# count the number of occurrences of an element in a list using count()

ratings = [2, 3, 1, 4, 3.5, 2, 2]

print(ratings.count(3.5))
print(ratings.count(2))

