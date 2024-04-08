prompt = "Enter a word to check if it's a palindrome! (enter 'quit' when you're done)"

words = []

while True:
  word = input(prompt)

  if word == 'quit':
    break
  else: 
    words.append(word)

for word in words:
  print(word)

for word in words:
  # print(word)
  letters = list(word)
  # print(letters)
  letters.reverse()
  string_from_list = "".join(letters)
  if string_from_list == word:
    print(f'Yep, {word} is a palindrome!')
  else:
    print(f'Nope, {word} is not a palindrome.')



