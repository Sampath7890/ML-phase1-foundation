"""
Take height (in metres) and weight (in kg) as input.
BMI = weight / height**2
Print BMI and category:
Below 18.5 → Underweight
18.5 to 24.9 → Normal
25 to 29.9 → Overweight
30 and above → Obese
"""

height = float(input("enter your height in meters: "))
weight = float(input("enter your weight: "))

bmi = weight / (height**2)

print(f"your BMI = {bmi}")

if bmi < 18.5 :
    print("underweight")
elif bmi <= 24.9 :
    print("normal")
elif bmi <= 29.9 :
    print("overweight")
else: 
    print("obese")            
