# Receive the following arguments from the user:
# Kilometers to drive
# Liters-per-kilometer usage of the car
# Price per liter of fuel
# Calculate the cost of the trip and display it to the user in the console. 
# Apply some of the string formatting tricks that you learned about in this course section.
user_distance = float(input("How many kilometers are you driving?:"))
user_km_avg = float(input("How many litres of gas does your car user per kilometer?:"))
user_gas_cost = float(input("What is the price of gas per liter?:"))
trip_cost = user_distance * user_km_avg * user_gas_cost
print(f"The cost of your trip will be ${trip_cost:.1f}.:")