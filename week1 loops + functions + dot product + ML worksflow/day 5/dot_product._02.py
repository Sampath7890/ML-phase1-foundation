"""Write a function dot_product(a, b) that:
→ takes two lists of same size
→ multiplies matching pairs using a loop
→ returns the final sum"""

"""Test with:
dot_product([1,2], [3,4])       → 11
dot_product([4,0], [0,3])       → 0
dot_product([1,2,3], [4,5,6])   → 32"""

def dot_product(a,b) :
    result = 0
    for i in range(len(a)) :
        result += a[i]*b[i]
    return result

a = []
b =[] 
 
n = int(input("dimensions = "))
for i in range(n) :
    a.append(int(input(f"enter A[{i}]")))
    b.append(int(input(f"enter B[{i}]")))

print(f"Vector A = {a}")
print(f"vector B = {b}")

print(f"dot product = {dot_product(a,b)}")