"""
Take units consumed as input.
Calculate bill:
0–100 units → ₹1.50 per unit
101–200 units → ₹2.50 per unit
201–300 units → ₹4.00 per unit
Above 300 → ₹6.00 per unit
Print total bill with f-string.
"""

units = float(input("enter how many units consumed: "))

if units <= 100 :
    bill = units*1.50
elif units <= 200 :
    bill = units * 2.50
elif units <=300 :
    bill = units * 3.50
else :
    bill = units*6.00

print(f"your bill for {units} units will be : {bill}")            
