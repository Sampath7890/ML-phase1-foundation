"""Write a function magnitude(v) that:
→ squares each element using a loop
→ sums them all
→ returns the square root (use ** 0.5)

Test with:
magnitude([3, 4])       → 5.0
magnitude([0, 0])       → 0.0
magnitude([1, 2, 2])    → 3.0"""

import math

def magnitude(v) :
    total = 0
    for num in v :
        total += num * num 
    return total**0.5



numbers = (input("enter vector: ")).split()
v = []
for num in numbers :
    v.append(int(num))

print(f"magnitude = {magnitude(v)}")

    
