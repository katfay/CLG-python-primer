prompt = "Please enter a dog species (enter 'quit' when you are done)"

dogs = []

while True:
  dog = input(prompt)

  if dog == 'quit':
    break
  else: 
    dogs.append(dog)

for dog in dogs:
  print(dog)