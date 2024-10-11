# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.
user_input = int(input("Enter any number between 0 nd 1,000,000,000: "))
while user_input < 0 or user_input > 1000000000:
    user_input = int(input("Enter any number between 0 and 1,000,000,000: "))
    if user_input >= 0 and user_input <= 1000000000:
        print(f"Your number is: {user_input}")
