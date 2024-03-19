word = input("Enter a word to check if is a palindrome!")
# print(word)
letters = list(word)
# print(letters)
letters.reverse()
string_from_list = "".join(letters)

if string_from_list == word:
  print(True) 
  print(f"Yep, '{word}' is a palindrome!")
else:
  print(False)
  print(f"Nope, '{word}' is not a palindrome, buddy. That's because '{word}' does not equal '{string_from_list}'.")
