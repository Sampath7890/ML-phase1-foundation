"""Write these functions properly with def and return:
add_vectors(v1, v2) — works for any size
scale_vector(v, scalar) — works for any size
magnitude(v) — returns the length
dot_product(v1, v2) — the one from today's math

Test all 4 with 2D and 3D vectors"""

import math
def add_vectors(v1,v2) :
    result =[]

    for i in range(len(v1)) :
        result.append(v1[i]+v2[i])
    return result

def scale_vectors(v, scalar) :
    result = []

    for i in range(len(v)) :
        result.append(v[i]*scalar)
    return result

def magnitude(v) :
    result = []
    total = 0

    for i in range(len(v)) : 
       total+=v[i]**2
       return math.sqrt(total)
    
v1_2d =[2 , 5]
v2_2d = [3,5]
print("======2d vectors=========")
print(f"addition of two vectors = {add_vectors(v1_2d,v2_2d)}")
print(f"scalar of a vector = {scale_vectors(v1_2d,3)}")
print(f"magnitude of a vectors = {magnitude(v1_2d)}")

v1_3d = [5,6,5]
v2_3d = [9,8,7]

print("======3d vectors=========")
print(f"addition of two vectors = {add_vectors(v1_3d,v2_3d)}")
print(f"scalar of a vector = {scale_vectors(v1_3d,3)}")
print(f"magnitude of a vectors = {magnitude(v1_3d)}")
