# Jeremiah Andrews
# 9/16/2024
# P3LAB
# Program that turns a float usd into largest denomination US currency,
# while making the remainder the next largest and so on.
import math


#get user's float input fo money
money = input("Enter the amount of money as a float: ")
money = float(money.replace("$", ""))
money = float(f"{money:.2f}")
#print(money)

#do math for all dollars and change
dollars = int(money)
change = round(money - dollars, 2)
remain_change = money - dollars
quarters = (remain_change*100)//25
remain_change = (change * 100)%25
dimes = remain_change//10
remain_change = remain_change%10
nickels = remain_change//5
remain_change = remain_change%5
pennies = remain_change

if dollars > 0:
    print(str(int(dollars)) + " Dollars")
if quarters > 0:
    print(str(int(quarters)) + " Quarters")
if quarters > 0:
    print(str(int(dimes)) + " Dimes")
if dimes > 0:
    print(str(int(nickels)) + " Nickels")
if nickels > 0:
    print(str(int(pennies)) + " Pennies")
if change == 0:
    print("No change")


