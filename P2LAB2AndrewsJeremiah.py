# Jeremiah Andrews
# 9/11/2024
# P2LAB2
# Program that creates a specified dictionary
import math
# make dictionary
cars = {"Camaro":18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
# get and print keys
keys = cars.keys()
print(keys)
print()
# get user's car of choice and print its mpg
user_car = input("Enter a vehicle to see it's mpg: ")
print()
print("The " + user_car + " gets " + str(cars[user_car]) + " mpg.")
print()
# get user's miles and calc then print gallons needed to drive that many miles
miles = int(input("How many miles will you drive the " + user_car + "?"))
print()
gal_needed = miles / cars[user_car]
print(str(round(gal_needed, 2)) + " gallons(s) of gas are needed to drive the " + str(user_car) + " " + str(miles) + " miles.")
