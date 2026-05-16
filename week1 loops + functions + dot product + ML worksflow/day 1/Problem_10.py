"""
Take a number as input. Print whether it is positive,
 negative, or zero. Also print whether it is even or odd.
"""

number = int(input("enter a number: "))
if(number > 0) :
    print(f"your number {number} is positive")
elif(number<0) :
    print(f"your number {number} is negative")
else :
    print(f"your number {number} is zero")    