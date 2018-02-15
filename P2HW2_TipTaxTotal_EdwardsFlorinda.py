# CTI-110 
# P2HW2 - Tip Tax Total 
# Florinda Edwards
# 02/15/2018

foodCost=float(input("Enter cost of food: "))
tipAmount=foodCost*0.18
salesTax=foodCost*0.07
totalCost=foodCost+tipAmount+salesTax

print("the tip is",format(tipAmount,'.2f'))
print("the sales tax is",format(salesTax,'.1f'))
print("the food cost",totalCost)
