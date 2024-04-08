def counting_vowels():
    prompt = "\nPlease enter your name\nEnter 'stop' when you're done\n\n"
    names = []
    while True:
        name = input(prompt)
        if name == 'stop':
            break
        else:
            names.append(name)
    for name in names:
        total_a = name.count('a')
        total_e = name.count('e')
        total_i = name.count('i')
        total_o = name.count('o')
        total_u = name.count('u')
        total_vowels = (total_a + total_e + total_i + total_o + total_u)
        if total_vowels == 1:
            print(f"{name}, your name has {total_vowels} vowel") 
        else:
            print(f"{name}, your name has {total_vowels} vowels")
