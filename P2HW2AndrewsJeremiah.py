# Jeremiah Andrews
# 9/15/2024
# P2HW2
# Grade set that you can specify certain aspects of grades with
import math
# make dictionary
grades = {"Module_One": "module_one", "Module_Two":"module_two", "Module_Three":"module_three", "Module_Four":"module_four", "Module_Five":"module_five", "Module_Six":"module_six"}
#keys = grades.keys()
#print(keys)
# prompt input for all module grades
grades["Module_One"] = float(input("Enter grade for Module 1: "))
grades["Module_Two"] = float(input("Enter grade for Module 2: "))
grades["Module_Three"] = float(input("Enter grade for Module 3: "))
grades["Module_Four"] = float(input("Enter grade for Module 4: "))
grades["Module_Five"] = float(input("Enter grade for Module 5: "))
grades["Module_Six"] = float(input("Enter grade for Module 6: "))
print()
#calc results for low high sum and average
lowest = min(grades["Module_One"], grades["Module_Two"], grades["Module_Three"], grades["Module_Four"], grades["Module_Five"], grades["Module_Six"])
highest = max(grades["Module_One"], grades["Module_Two"], grades["Module_Three"], grades["Module_Four"], grades["Module_Five"], grades["Module_Six"])
grades_sum = grades["Module_One"] + grades["Module_Two"] + grades["Module_Three"] + grades["Module_Four"] + grades["Module_Five"] + grades["Module_Six"]
average = grades_sum/6

#print calulated numbers
print("-------------------Results-------------------")
print("Lowest Grade::     " + str(lowest))
print("Highest Grade:     " + str(highest))
print("Sum of Grades:     " + str(grades_sum))
print("Average:           " + str(f"{average:.2f}"))
print("---------------------------------------------")
