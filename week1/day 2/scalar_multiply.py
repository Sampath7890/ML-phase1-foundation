"""
Take a vector and a scalar as input.
Print the result of multiplying.
Also print: "Arrow got longer" or "Arrow got shorter"
depending on whether scalar > 1 or scalar < 1
"""

v1 = int(input("enter vector v1 :"))
v2 = int(input("enter vector v2 :"))

print(f"your vector = [{v1} , {v2}]")
scalar = int(input("enter a scalar: "))
print(f"your scalar = {scalar}")

result_v1 = scalar * v1
result_v2 = scalar * v2

print(f"{result_v1 , result_v2}")

if(scalar > 1) :
    print(f"arrow will get longer")
elif 0 < scalar < 1  :
    print("arrow will got shorter")
elif scalar == 1 :
    print("arrow will remain same") 
elif scalar == 0 :
    print("arrow will become zero vector")     


else :
    print("arrow direction is flipped")    