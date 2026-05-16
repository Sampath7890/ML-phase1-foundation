"""
Take a 2D vector as input.
A unit vector = divide each element by the magnitude.
Result always has magnitude = 1.
Print the original vector, its magnitude,
and the unit vector.
Example:
v = [3, 4] → magnitude = 5.0
unit = [3/5, 4/5] = [0.6, 0.8]
"""
v1_x = int(input("enter vector v1 x: "))
v1_y = int(input("enter vector v1 y: "))
print(f"vector 1 = [{v1_x},{v1_y}]")

magnitude_v1 = (v1_x**2 + v1_y**2) ** 0.5

print(f"the magnitude of vector [{v1_x},{v1_y}] = {magnitude_v1}")

unit_v1_x = v1_x / magnitude_v1
unit_v1_y = v1_y / magnitude_v1

print(f"v = [{unit_v1_x},{unit_v1_y}] = [{unit_v1_x},{unit_v1_y}] ")