# Create a function vowel_counting to loop through a string parameter and print to console how many vowels(“A”, “E”, “I”, “O”, “U” ) are in the argument. Save it in a module.



# Import the module you just saved. Call the function and pass your name as the argument.

# The output may look like this: 

# My full name is Bing Li.

# I have 2 vowels in my name.


# import ask_name
# import find_vowels
# import is_alpha
# import vowel_count

# import get_names
# import calculate_vowels

prompt = "\nPlease enter your name\nEnter 'stop' when you're done\n\n"

names = []

# counter = []

while True:
    name = input(prompt)

    if name == 'stop':
        break
    else:
        names.append(name)

for name in names:
    # print(name)
    total_a = name.count('a')
    total_e = name.count('e')
    total_i = name.count('i')
    total_o = name.count('o')
    total_u = name.count('u')
#    print(total_a, total_e, total_i, total_o, total_u)
    total_vowels = (total_a + total_e + total_i + total_o + total_u)
    # print(total_vowels)
    print(f"{name}, your name has {total_vowels} vowels") 


#    letters = list(name)
#    print(letters) 
#    for letters in name:
#        if letters == 'a':
#            counter.append(1)
#        elif letters == 'e':
#            counter.append(1)
#        elif letters == 'i':
#            counter.append(1)
#        elif letters == 'o':
#            counter.append(1)
#        elif letters == 'u':
#            counter.append(1)
#    if 
            

# def find_vowels():
#     for user_name 

# def vowel_message():
#    print(f"Your name has {how_many} vowels.")




#enter_name('Katherine')
#enter_name('Lewis')
# enter_name('Duncan')



# if XXX == "a" OR if XXX == "e" or if XXX == "i" or if XXX == "o" or if XXXX == "u":
    