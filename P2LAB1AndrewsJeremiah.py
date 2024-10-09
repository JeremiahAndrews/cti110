# Jeremiah Andrews
# 9/11/2024
# P2LAB1
# Calculate math related to a circle
import math

#get radius input and do the math for diameter, circumfrence & area, then print
radius = float(input("What is the radius of the circle?"))
diameter = radius * 2
print()
print("The diameter of the circle is " + str(round(diameter, 1)))
circumfrence = radius * 2 * math.pi
print()
print("The circumfrence of the circle is " + str(round(circumfrence, 2)))
area = math.pi * (math.pow(radius, 2))
print()
print("The area of the circle is " + str(round(area, 3)))
