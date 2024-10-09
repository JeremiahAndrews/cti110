# P4LAB1
# Jeremiah Andrews
# 9/25/2024
# Grade set that you can specify certain aspects of grades with and compile
import math
module_num = 0
grade_num = int(input("How many scores do you want to enter? "))
# make list and append user inputs
grades = []
for i in range(grade_num):
    module_num += 1
    latest_grade = float(input("Enter score #" + str(module_num) + ": "))
    if latest_grade >= 0 and latest_grade <= 100:
        grades.append(latest_grade)
        print("top if entered")
    elif latest_grade < 0 or latest_grade > 100:
        print("bad if entered")
        while latest_grade < 0 or latest_grade > 100:
            print("INVALID Score entered!!!!")
            print("Score should be from 0 through 100")
            latest_grade = float(input("Enter score #" + str(module_num) + " again: "))
        grades.append(latest_grade)
#calc results for low high sum and average
lowest = min(grades)
grades.remove(min(grades))
highest = max(grades)
grades_sum = sum(grades)
average = grades_sum/len(grades)
#if statement to determine letter grade
let_grade = str
if average < 60:
    let_grade = "F"
elif average < 70:
    let_grade = "D"
elif average < 80:
    let_grade = "C"
elif average < 90:
    let_grade = "B"
elif average >= 90:
    let_grade = "A"


#print calulated numbers
print("-------------------Results-------------------")
print("Lowest Grade  :     " + str(lowest))
print("Modified List :     " + str(grades))
print("Scores Average:     " + str(f"{average:.2f}"))
print("Grade         :     " + let_grade)
print("---------------------------------------------")
