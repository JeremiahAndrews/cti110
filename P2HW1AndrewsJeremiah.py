# Jeremiah Andrews
# 9/8/2024
# P1HW2
#  Travel Calc

# set all the variables and get values from user
print("This program calculates and displays travel expenses.")
print()
budget = float(input("Enter your budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? Input here: "))
print()
housing = float(input("How much will you need for temporary housing? Input here:"))
print()
food = float(input("How much will you need for food? Input here:"))
print()
# compile user given values and print
print("---------------Travel Expenses---------------")
print("Location:          " + destination)
print("Starting budget:   $" + str(f"{budget:.2f}"))
print("Fuel:              $" + str(f"{gas:.2f}"))
print("Housing:           $" + str(f"{housing:.2f}"))
print("Food:              $" + str(f"{food:.2f}"))
print("---------------------------------------------")
print()

# calc final balance and print that too
remaining = budget - gas - housing - food
print("Remaining Balance: $" + str(remaining))
