# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
user_investment = float(input("Enter the investment amount: "))
user_interest = float(input("Enter the interest rate in percentage: "))
user_years = int(input("Enter the number of years to invest: "))
future_value = user_investment * (1 + user_interest / 100) ** user_years
print(f"The future value of your investment will be: {future_value}")
