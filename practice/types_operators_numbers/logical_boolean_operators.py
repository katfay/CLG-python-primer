# takes one or two boolean opeators and outputs another boolean value

# and
# and operator - boolean/logical operator
# checks if the values on the left and right are BOTH true
# e.g. 

result = True and True

result2 = True and False

result3 = False and False

result4 = False and True

print(result)

print(result2)

print(result3)

print(result4)

# or
# or operator - boolean/logical operator
# checks if at least ONE of the values on the left or right is true


result5 = True or True

result6 = True or False

result7 = False or False

result8 = False or True

print(result5)

print(result6)

print(result7)

print(result8)

print(f"The output of 'True or True' is expected to be true and is actually ... {result5}")
print(f"The output of 'True or False' is expected to be true and is actually ... {result6}")
print(f"The output of 'False or False' is expected to be false and is actually ... {result7}")
print(f"The output of 'False or True' is expected to be true and is actually ... {result8}")

# not
# not operator - boolean/logical operator
# checks if the input is not true - negates an input
# e.g. not True = False; not False = True


result9 = not False

result10 = not True

print(result9)

print(result10)

print(f"The output of 'not False' is expected to be True and is actually ... {result9}")
print(f"The output of 'not True' is expected to be False and is actually ... {result10}")

is_patrolled = True

has_sharks = False

# first attempt to show if beach is safe
is_beach_safe = is_patrolled and has_sharks

print(is_beach_safe)

is_beach_safe2 = is_patrolled and (not has_sharks)

print(is_beach_safe2)

has_licence = True

age = 21

can_drive = has_licence and (age >= 21)

print(can_drive)