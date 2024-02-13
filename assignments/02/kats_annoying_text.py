original_text = "This is the First Edition of the text."
shouting_text = original_text.upper()
annoying_text = 10 * shouting_text
annoying_length = str(len(f"{annoying_text}"))

# Check shouting_text variable prints in upper case
# print(shouting_text)

# Check annoying_text variable prints correctly
# print(annoying_text)

# Check character length prints as string
# print(annoying_length)

print(f"\nMy annoying text is {annoying_text}\n")

# print("It has " + annoying_length + " characters.\n")

# Refactor the above print parameter to f-string / template literal
print(f"It has {annoying_length} characters.\n")