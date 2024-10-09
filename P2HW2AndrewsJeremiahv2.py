# Jeremiah Andrews
# 9/15/2024
# P2HW2
# Grade set that you can specify certain aspects of grades with
import math
# prompt input for all module grades
Module_One = float(input("Enter grade for Module 1: "))
Module_Two = float(input("Enter grade for Module 2: "))
Module_Three = float(input("Enter grade for Module 3: "))
Module_Four = float(input("Enter grade for Module 4: "))
Module_Five = float(input("Enter grade for Module 5: "))
Module_Six = float(input("Enter grade for Module 6: "))
# make list and append user inputs
grades = []
grades.append(Module_One)
grades.append(Module_Two)
grades.append(Module_Three)
grades.append(Module_Four)
grades.append(Module_Five)
grades.append(Module_Six)
#calc results for low high sum and average
lowest = min(grades)
highest = max(grades)
grades_sum = sum(grades)
average = grades_sum/len(grades)
#print calulated numbers
print("-------------------Results-------------------")
print("Lowest Grade::     " + str(lowest))
print("Highest Grade:     " + str(highest))
print("Sum of Grades:     " + str(grades_sum))
print("Average:           " + str(f"{average:.2f}"))
print("---------------------------------------------")




Module_One, Module_Two, Module_Three, Module_Four, Module_Five, Module_Six
