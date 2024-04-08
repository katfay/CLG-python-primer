# Create a variable with your name.

kat = {}

# Assign a dictionary to the variable with your information (age, occupation, hobby, etc).

kat = {'age': '39', 'occupation': 'devOps project officer', 'hobby': 'surfing', 'pet': 'duncan'}

#Use for loop to iterate through the dictionary and F-string to print each key value pairs (eg. “My favourite color is green.”)

for key, value in kat.items():
  print(f'My {key} is {value}')

# Try add, delete, update and clear data from your dictionary.
  
kat['2nd language'] = 'French'

kat['hobby'] = 'snowboarding'

kat.pop('occupation')

print(kat.items())