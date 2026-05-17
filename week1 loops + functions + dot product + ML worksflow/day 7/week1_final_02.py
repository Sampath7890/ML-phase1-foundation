#Write dot_product(a, b) function

def dot_product(a,b) :
    result = 0
    for i in range(len(a)) :
        result += a[i] * b[i]
    return result

a = []
b = []

n = int(input("enter dimensions:"))

for i in range(n) :
    value_a = int(input("enter vector a : "))
    a.append(value_a)


for i in range(n) :
    value_b= int(input("enter vector b : "))
    b.append(value_b)

answer = dot_product(a,b)

print(f"dot product = {answer}")

