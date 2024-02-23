# Get base savings value
money_start = input("\nEnter the amount of money you already have saved (use numbers only): \n")

# Handle ValueError in input
try:
    money_start = float(money_start)
except ValueError:
    print("DEV MSG: money_start input could not be converted to float because the user's string input did not represent a valid float value (e.g. it contained words or symbols)")

# Convert input type to float 
if type(money_start) != float:
    money_start_retry = input("\nEnsure you use only numerical characters. Try again to enter the amount of money you already have saved, but use only numbers (not words or symbols): \n")
    money_start_retry = float(money_start_retry)
    money_start = money_start_retry
    print(f"DEV MSG: Amount {money_start} was converted to float on 2nd input")
else:
    print(f"DEV MSG: Amount {money_start} was converted to float on 1st input")

# Get number of years user will save for
saving_years = input("\nEnter the number of years you will be saving to meet your goal: \n")

# Handle ValueError in input
try:
    saving_years = int(saving_years)
except ValueError:
    print("DEV MSG: saving_years input could not be converted to integer because the user's string input did not represent a valid integer value (e.g. it contained words or symbols)")

# Convert saving_years value type to integer
if type(saving_years) != int:
    saving_years_retry = input("\nUse only numerical characters and whole numbers (do not use not words or demicals) to enter the number of years you are going to save for your goal: \n")
    saving_years_retry = int(saving_years_retry)
    saving_years = saving_years_retry
    print(f"DEV MSG: Years ({saving_years}) was converted to integer on 2nd input")
else:
    print(f"DEV MSG: Years ({saving_years}) was converted to integer on 1st input")

# Get interest rate
interest_rate = input("\n Enter the current cash interest rate (but don't include the '%' symbol): \n")

# Handle ValueError in input
try:
    interest_rate = float(interest_rate)
except ValueError:
    print("DEV MSG: interest_rate input could not be converted to float because the user's string input did not represent a valid float value (e.g. it contained words or symbols)")

# Convert interest_rate value type to float
if type(interest_rate) != float:
    interest_rate_retry = input("\nUse only numerical characters and decimal points (do not use not words or symbols including '%') to enter the interest rate: \n")
    interest_rate_retry = int(interest_rate_retry)
    interest_rate = interest_rate_retry
    print(f"DEV MSG: Interest rate {interest_rate}% was converted to float on 2nd input")
else:
    print(f"DEV MSG: Interest rate {interest_rate}% was converted to float on 1st input")

# Prevent error in savings calculations that will occur if user inputs the interest rate formatted as .0599 instead of 5.99 (%), etc
if interest_rate < 0.50:
    interest_rate = interest_rate * 100
    print(f"DEV MSG: The interest rate is now expressed as {interest_rate}%")
else:
    print(f"DEV MSG: No change to factor of interest rate was needed.")

# Express the interest rate in demical places
interest_rate = interest_rate / 100  

# Calculate additional savings created from interest
savings_from_interest = money_start * interest_rate * saving_years

# Calulcate total savings amount
money_result = money_start + savings_from_interest

# Explain the savings result and breakdown to the user
print(f"\nWith a base of ${money_start} in savings, after {saving_years} years, your savings will be ${money_result}. Awesome! \n \n This includes ${savings_from_interest} in savings from the interest alone.\n")

# Show (in booelan) in the console whether the savings result is over $10000 

if money_result >= 10000:
    print(True)
else:
    print(False)