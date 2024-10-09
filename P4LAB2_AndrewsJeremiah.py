# P4LAB1
# Jeremiah Andrews
# 9/25/2024
# A program that requests a positive integer and gives its multiplication equations 1-12
import math
run = "yes"
increment = 0
integer = int(input("Enter an integer:"))
while run == "yes":
    print()
    if integer < 0:
        print("This program does not handle negative numbers.")
        print()
        run = input("Would you like to run the program again? ")
        print()
        if run == "yes":
            integer = int(input("Enter an integer:"))
    else:
        for num in range(12):
            increment += 1
            plus = integer * increment
            print(str(integer) + " * " + str(increment) + " = " + str(plus))
        increment = 0
        print()
        run = input("Would you like to run the program again? ")
        print()
        if run == "yes":
            integer = int(input("Enter an integer:"))
print("Exiting program...")
