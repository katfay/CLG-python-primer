# Initialise three variables: money_start, saving_years, interest_rate
# Assign the values to the three variables using the input() function. Pass an instructional message (string) as an argument to the input function.
# Convert each input to a float or integer, depending on the type of input you are requesting.

# Initialise money_start variable and assign input value using an instructional msg as an argument
money_start = input("\nEnter the amount of money you already have saved (use numbers only): \n")

# Convert money_start value type to integer and hendle 1 x input type error.

# 1ST EFFORTS TO HANDLE STRING VALUE ERROR:

# money_type = print(type(money_start))

# if money_type != int:
#    print("Amount of money is not an integer")
# else:
#    print(f"Amount is money is an integer and it is ${money_start}")

# Convert money_start to int

# money_start = int(money_start)
# print(money_start)
# print(type(money_start))

# Handle failure to convert string to int

# is_amount_int = type(money_start) ==  int
# print(f"is_amount_int result is {is_amount_int}")

# can_convert_amount = type()

#if ( (SUCCESS CONVERTING STR TO INT = TRUE) is_amount_int != True:
#    money_start_retry = input("Ensure you use only numerical characters. Enter #the amount of money you already have saved: ")
#    money_start_retry = int(money_start_retry)
#    money_start = money_start_retry
#    print(f"Amount {money_start} was converted to int on 2nd input")
#else:
#    print(f"Amount {money_start} was converted to int on 1st input")

# Convert money_start to ing

# money_start = int(money_start)
 
# print(money_start)
# print(type(money_start))



# 2ND  EFFORTS TO HANDLE STRING VALUE ERROR (STACK OVERFLOW):

# TO-DO!! add if / else statement to convert to int 
# TO-DO!! and remove $ - other solution found
# TO-DO!! and round down to nearest $ - other solution found

try:
    money_start = int(money_start)
except ValueError:
    print("DEV MSG: money_start input could not be converted to integer because the user's string input did not represent a valid integer value (e.g. it contained words or symbols)")

if type(money_start) != int:
    money_start_retry = input("\nEnsure you use only numerical characters. Try again to enter the amount of money you already have saved, but use only numbers (not words or symbols): \n")
    money_start_retry = int(money_start_retry)
    money_start = money_start_retry
    print(f"DEV MSG: Amount {money_start} was converted to integer on 2nd input")
else:
    print(f"DEV MSG: Amount {money_start} was converted to integer on 1st input")


# Initialise saving_years variable and assign input value using an instructional msg as an argument
saving_years = input("\nEnter the number of years you will be saving to meet your goal: \n")

# Convert saving_years value type to integer and hendle 1 x input type error.
try:
    saving_years = int(saving_years)
except ValueError:
    print("DEV MSG: saving_years input could not be converted to integer because the user's string input did not represent a valid integer value (e.g. it contained words or symbols)")

if type(saving_years) != int:
    saving_years_retry = input("\nUse only numerical characters and whole numbers (do not use not words or demicals) to enter the number of years you are going to save for your goal: \n")
    saving_years_retry = int(saving_years_retry)
    saving_years = saving_years_retry
    print(f"DEV MSG: Years ({saving_years}) was converted to integer on 2nd input")
else:
    print(f"DEV MSG: Years ({saving_years}) was converted to integer on 1st input")

# Initialise interest_rate variable and assign input value using an instructional msg as an argument
interest_rate = input("\n Enter the current cash interest rate (but don't include the '%' symbol): \n")

# TO-DO!! add if / else statement to convert string to integer/float
# TO-DO!! add if / else statement to remove percentage - other solution found
# TO-DO!! add if / else statement to convert to float 

# Convert interest_rate value type to integer and hendle 1 x input type error.
try:
    interest_rate = float(interest_rate)
except ValueError:
    print("DEV MSG: interest_rate input could not be converted to float because the user's string input did not represent a valid float value (e.g. it contained words or symbols)")

if type(interest_rate) != float:
    interest_rate_retry = input("\nUse only numerical characters and decimal points (do not use not words or symbols including '%') to enter the interest rate: \n")
    interest_rate_retry = int(interest_rate_retry)
    interest_rate = interest_rate_retry
    print(f"DEV MSG: Interest rate {interest_rate}% was converted to float on 2nd input")
else:
    print(f"DEV MSG: Interest rate {interest_rate}% was converted to float on 1st input")

# Handle input of interest rate expressed as .05 etc
if interest_rate < 0.50:
    interest_rate = interest_rate * 100
    print(f"DEV MSG: The interest rate is now expressed as {interest_rate}%")
else:
    print(f"DEV MSG: No change to factor of interest rate was needed.")

# Create a variable money_result
# Assign the formula money_start * interest_rate * saving_years to money_result
interest_rate = interest_rate / 100  
savings_from_interest = money_start * interest_rate * saving_years
money_result = money_start + savings_from_interest

# Print money_result to the console in a formatted string.
print(f"\nWith a base of ${money_start} in savings, after {saving_years} years, your savings will be ${money_result}. Awesome! \n \n This includes ${savings_from_interest} in savings from the interest alone.\n500")

# Is the result more than 10000? If yes, include in your code to print True to the console, otherwise print False.

if money_result >= 10000:
    print(True)
else:
    print(False)

# TO-DO!! refactor so that money_start is converted to a float, not integer? Will result in fewer errors as type input includes whole numbers and decimals?