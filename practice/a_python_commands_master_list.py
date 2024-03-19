#       {}
# aka: braces / squiggly brackets
# WRAP A VARIABLE inside a string using braces/squiggly brackets (in conjunction with f-string command)

# """
# aka: triple quotes
# MULTILINE string

# + 
# aka: plus
# adds one object to another 
# includes adding integers in mathematical equations
# includes concactenating objects (strings and variables) to print string e.g. variable = "kat"; print("My name is " + variable) [prints: "My name is Kat"]

# *
# aka: multiplier
# multiple the value of the object (integer, string, etc.)
# e.g. variable = kat; print(4 * variable) [prints: katkatkatkat] 

#       **
# exponential operator - raise one number to the power of another
# e.g. print(5 ** 3) [prints: 125]

#       % 
# modulo operator - identify the remainder (modulus) when one number is divided by another
# e.g. print(25 % 4) [prints: 1]

#       //
# floor division operator - identify the resulting whole number (equal or lower to the result) of one number divided by another 
# e.g. print(27 // 6) [prints: 4]

#       >
# greater than comparison operator

#       <
# less than comparison operator

#       >=
# greater than or equal to comparison operator

#       <=
# less than or equal to comparison operator

#       ==
# equal to comparison operator

#       !=      
# not equal to comparison operator      

#       BODMAS
# order of precedence of operators follows BODMAS
# (B)rackets, (O)rders [exponentials], (D)ivision, (M)ultiplication, (A)ddition, (S)ubtraction 
# So: ()        >       **      >       /, *, //, %         > +, -

and
# and operator - boolean/logical operator
# checks if the values on the left and right are BOTH true
# e.g. variable = True and True; print(variable) [prints: True]
# e.g. variable2 = False and True; print(variable2) [prints: False]

append()
# function to add only 1 item to the end of a list
# e.g. pets = ['ants', 'bird', 'cat', 'dog']; pets.append('Duncan'); print(pets) [prints: ['ants', 'bird', 'cat', 'dog', 'Duncan']]

count()
# count the number of occurrences of an element in a list using count()
# e.g. ratings = [2, 3, 1, 4, 3.5, 2, 2]; print(ratings.count(3.5)); [prints [1]]


del
# function to delete one or multiple list items
# pets = ['ants', 'bird', 'cat', 'dog']; del pets[0:2]; print(pets) [prints: ['cat', 'dog']]

extend()
# add one list to another list; pass the additional list as a parameter
# e.g. pets = ['ants', 'bird', 'cat', 'dog']; farm_animals = ['sheep', 'goat', 'cows']; pets.extend(farm_animals); print(pets) [prints: ['ants', 'bird', 'cat', 'dog', 'sheep', 'goat', 'cows']]

f
# INSERT A VARIABLE INTO STRING using an f-string (in conjunction with braces/squiggly brackets)
# e.g. variable = kat; print(f("My name is {variable}")) [prints: "My name is kat"]

find()
# use the find() method to search for substrings in a string using the find() method. It returns the index of the first occurrence of the substring
# e.g. email = 'bing@outlook.com'; domain_index = email.find('outlook.com'); print(domain_index) [prints: '5']
# note if substring is not found, find() method returns -1

in
# in operator - for lists
# e.g. pets = ['bird', 'cat', 'dog']; print('dog' in pets); [prints: True]

input()
# tbc

insert()
# function to add an item to the middle of a list
# e.g. pets = ['ants', 'bird', 'cat', 'dog']; pets.insert(1, 'Duncan'); print(pets) [prints: ['ants', 'Duncan', 'bird', 'cat', 'dog']]
isalpha()
# isalpha() method checks if a string contains only letters 
# e.g. a = "abcd"; b = " "; c = "12fad"; d = "apple orange"; print(a.isalpha()); print(b.isalpha()); print(c.isalpha()); print(d.isalpha()); [prints: True, False, False, False]


len 
# function
# print the LENGTH of string or list (number of elements in that list)
# e.g. print(len("parameter")) [prints: 9]
# e.g. pets = ["Duncan", "Chessie", "Eric", "fish"]; print(len(pets)); [prints: [4]]

.lower()
# print the variable in LOWER CASE
# e.g. variable = "Hey!"; print(variable.lower()) [prints: "hey!"]


/n
# LINE BREAK


not
# not operator - boolean/logical operator
# checks if the input is not true - negates an input
# not True = False; not False = True
# e.g. variable = not False; print(variable) [prints: True]
# e.g. variable = not True; print (variable) [prints: False]

not in 
# not in operator - lists
# e.g. pets = ['bird', 'cat', 'dog']; print('Duncan' not in pets); [prints: True]

or
# or operator - boolean/logical operator
# checks if at least ONE of the values on the left or right is true
# e.g. variable = True or False; print(variable) [prints: True]
# e.g. variable = False or False; print(variable) [prints: False]
 
pop()
# function to remove an element from a list and return it individually
# note this function removes the popped item from the original list. Next time you print the original list, it won't contain that popped item.
# e.g. pets = ['ants', 'bird', 'cat', 'dog']; pet = pets.pop(2); print(pet); print(pets) [prints: cat [new line] 'ants', 'bird', 'dog']
# if no parameter given for index number (e.g. pet = pets.pop()), default -1 is used [removes last list item]

print()
# PRINT
# write text output to the console 

remove()
# function to remove 1 x list element only 
# e.g. pets = ['ants', 'bird', 'cat', 'dog']; pets.remove('cat'); print(pets) [prints: 'ants', 'bird', 'dog']

# replace() method
# replace one substring with another, 1st argument is substring you want replaced, 2nd argument is substring you want to replace the 1st with
# e.g. email = 'bing@outlook.com'; gmail = email.replace('outlook.com', 'gmail.com'); print(gmail) [prints: 'bing@gmail.com']

reverse()
# reverse sort a list of numbers or str from its existing state 
# e.g. numbers = [12, 3, -3, -3.45, 0, 192]; numbers.reverse(); print(numbers) [prints: [12, 3, -3, -3.45, 0, 192]]
# e.g. pets = ["Duncan", "Chessie", "Eric", "fish"]; print(pets); pets.reverse(); print(pets) [prints: ['fish', 'Eric', 'Chessie', 'Duncan']]

# slice notation - pets[1:3] = ['Duncan', 'dog2']
# replaces multiple list items 
# e.g. pets = ['bird', 'cat', 'dog', 'canary', 'fish', 'horse']; pets[1:3] =['Duncan', 'dog2']; print(pets) [prints: 'bird', 'Duncan', 'dog2', 'canary', 'fish', 'horse']

# slice range - list_name[start:stop]
# print the elements from the start index up to and not including the stop index 
# e.g. sale = ['hat', 'bathers', 'surfboard', 'hair wax', 'sunscreen', 'wetsuit', 'drinkbottle', 'snacks']; print(sale[1:3]) [prints: bathers, surfboard] 

sort()
# sort list of numbers in asc numerical order; sort list of strings in alpha order 
# e.g. numbers = [12, 3, -3, -3.45, 0, 192]; numbers.sort(); print(numbers) prints: [[-3.45, -3, 0, 3, 12, 192]]
# e.g. pets = ["Duncan", "Chessie", "Eric", "fish"]; pets.sort(); print(pets) [prints: ['Chessie', 'Duncan', 'Eric', 'fish']]

# string indexes
# get individual characters from a string by using indexes
# e.g. title = 'Duncan is great'; print(title[4]) [prints: 'a']

# string slice notation
# slice a string and return the sliced portion
# e.g. title = 'Duncan is great'; print(title[-5:]) [prints: 'great']
# e.g. print(title[0:6]) [prints: 'Duncan']``

type()
# identifies the type of data (string, integer, float, boolean)
# e.g. dog_name = "duncan"; print(type(dog_name)) [prints: "<class 'str'>"] 

.upper()
# print the variable in UPPER CASE
# e.g. variable = "hey!"; print(variable.upper()) [prints: "HEY!"]


