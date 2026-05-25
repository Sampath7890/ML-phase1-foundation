"""
Take a person's birth year as input. Calculate their age. Print whether they are
 a child (below 13), teenager (13–17), adult (18–59), or senior (60+).
"""

year = int(input("enter your birth year: "))
age = 2026 - year

if(age <= 13) :
    print(f"your age is {age} and you are child")
elif(age <= 17) :
    print(f"your age is {age} and you are teenager")
elif(age <= 59) :
    print(f"your age is {age} and you are adult")
else:
    print(f"your age is {age} and you are senior")