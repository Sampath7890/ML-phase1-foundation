"""
Take two numbers as input. Print which one is bigger. If they're equal, print "Both are equal."
"""

num1 = int(input("enter a num1: "))
num2 = int(input("enter a num2: "))
if(num1<num2) :
    print(f"num2 {num2} is greater") 
elif(num1>num2) :
    print(f"num1 {num1} is greater")
else :
     print(f"numbers {num1} and {num2} are EQUAL")
     