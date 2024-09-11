# Jeremiah Andrews
# 9/8/2024
# P1HW2
#  Travel Calc

# set all the variables and get values from user
print("This program calculates and displays travel expenses.")
budget = int(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? Input here: "))
housing = int(input("How much will you need for temporary housing? Input here:"))
food = int(input("How much will you need for food? Input here:"))

# compile user given values and print
print("-----Travel Expenses-----")
print("Location: " + destination)
print("Starting budget: " + str(budget))
print()
print("Fuel: " + str(gas))
print("Housing: " + str(housing))
print("Food: " + str(food))
print()

# calc final balance and print that too
remaining = budget - gas - housing - food
print("Remaining Balance: " + str(remaining))
