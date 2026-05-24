#Write dot_product(v1, v2) using only lists and a loop. Then verify it gives the same answer as np.dot().
import numpy as np
def dot_product(v1, v2) :
    total = 0
    for i in range(len(v1)) :
        total += v1[i] * v2[i]
    return total
    


v1 = [2, 3, 5]
v2 = [4, 1, 2]

manual = dot_product(v1 , v2)
numpy_result = np.dot(v1,v2)

print(f"manual = {manual}")
print(f"numpy result = {numpy_result}")
print(f"match = {manual==numpy_result}")