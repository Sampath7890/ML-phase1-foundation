"""
Take a vector [a, b] as input from the user.
Print:
- The vector
- Its magnitude (length)
- Whether it points right or left (x > 0 or x < 0)
- Whether it points up or down (y > 0 or y < 0)
"""
import math

a = int(input("enter vector a: "))
b = int(input("enter vector b: "))

magnitude = math.sqrt(a**2 +b**2)

print(f"the given vector = [{a},{b}]")
print(f"the magnitude of vector [{a},{b} = {magnitude}]")

if a > 0 :
    print("it points to right")
elif a < 0 :
    print("it points left")
elif b > 0 :
    print("it points up")
elif b < 0 :
    print("it points down")            