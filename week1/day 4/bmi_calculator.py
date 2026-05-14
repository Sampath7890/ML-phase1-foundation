"""P7 — bmi.py Medium
Write calculate_bmi(weight, height) and get_category(bmi)
Two separate functions.
calculate_bmi returns the number.
get_category takes that number and returns: "Underweight", "Normal", "Overweight", "Obese"
Call both together to give a full result.
"""
def calculate_bmi(weight, height) :
    return weight / (height**2)

def get_category(bmi) :
    if bmi <= 18.5 :
        return "underweight"
    elif bmi <= 24.9 :
        return "normal"
    elif bmi <= 29.9 :
        return "overweight"
    else :
        return "obese"

weight = int(input("enter your weight: ")) 
height = float(input("enter your height: "))    

bmi = calculate_bmi(weight,height)

print(f"your bmi = {calculate_bmi(weight,height)} and you are {get_category(bmi)}")

