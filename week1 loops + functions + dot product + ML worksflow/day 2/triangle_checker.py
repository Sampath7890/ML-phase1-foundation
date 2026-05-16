"""
Take 3 sides of a triangle as input.
Check if they form a valid triangle.
Rule: sum of any two sides must be
greater than the third side.
If valid: also check if it is
equilateral (all equal),
isoceles (two equal),
or scalene (all different).
"""

x = int(input("traingle side 1 : " ))
y = int(input("traingle side 2 : " ))
z = int(input("traingle side 3 : " ))

if(x+y>z and x+z>y and y+z>x) :
    print("it is a valid traingle")
else:
    print("not a valid trainglle")

if x==y==z :
    print("equilateral traingle")
elif x==y or y==z or z==x:
    print("isoceles traingle")
else :
    print("scalane traingle")



