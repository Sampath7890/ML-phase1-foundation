import math

def dot_product(a, b):
    result = 0

    for i in range(len(a)):
        result += a[i] * b[i]

    return result


def magnitude(vector):
    total = 0

    for num in vector:
        total += num * num

    return math.sqrt(total)


def cosine_similarity(a, b):
    dot = dot_product(a, b)

    mag_a = magnitude(a)
    mag_b = magnitude(b)

    return dot / (mag_a * mag_b)


a = []
b = []

n = int(input("dimensions = "))

for i in range(n):
    a.append(int(input(f"Enter A[{i}] = ")))
    b.append(int(input(f"Enter B[{i}] = ")))


print(f"Vector A = {a}")
print(f"Vector B = {b}")

print(f"Dot Product = {dot_product(a, b)}")
print(f"Cosine Similarity = {cosine_similarity(a, b)}")