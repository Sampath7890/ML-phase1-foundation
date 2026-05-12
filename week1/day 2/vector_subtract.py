"""
Take two 2D vectors as input.
Subtract v2 from v1.
Print the result.
Also print: "v1 is bigger" or "v2 is bigger"
based on which has greater magnitude.
Formula magnitude: (x**2 + y**2) ** 0.5
"""

v1_x = int(input("enter vector v1 x : "))
v1_y = int(input("enter vector v1 y : "))
print(f"given vector = [{v1_x},{v1_y}]")

v2_x = int(input("enter vector v2 x : "))
v2_y = int(input("enter vector v2 y : "))
print(f"given vector = [{v2_x},{v2_y}]")

subtract_v1 = v1_x - v1_y 
subtract_v2 = v2_x - v2_y 

print(f"result = [{subtract_v1},{subtract_v2}]")

magnitude_v1 = (v1_x**2 + v1_y**2) ** 0.5
magnitude_v2 = (v2_x**2 + v2_y**2) ** 0.5

print(f"magnitude of v1 [{v1_x},{v1_y}] = {magnitude_v1} ")
print(f"magnitude of v2 [{v2_x},{v2_y}] = {magnitude_v2} ")

if magnitude_v1 > magnitude_v2 :
    print("v1 is bigger")
else:
    print("v2 is bigger")

