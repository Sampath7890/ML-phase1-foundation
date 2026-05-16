"""
Take two 2D vectors as input from the user.
Print their sum.
Example:
Enter v1 x: 3
Enter v1 y: 4
Enter v2 x: 1
Enter v2 y: 2
Result: [4, 6]
"""

v1_x = int(input("enter vector v1 x: "))
v1_y = int(input("enter vector v1 y: "))
print(f"vector 1 = [{v1_x},{v1_y}]")

v2_x = int(input("enter vector v2 x: "))
v2_y = int(input("enter vector v2 y: "))
print(f"vector 1 = [{v2_x},{v2_y}]")

result_x = v1_x + v2_x
result_y = v1_y + v2_y

print(f"addition of vector [{v1_x},{v1_y}] and [{v2_x},{v2_y}] = [{result_x},{result_y}]")
