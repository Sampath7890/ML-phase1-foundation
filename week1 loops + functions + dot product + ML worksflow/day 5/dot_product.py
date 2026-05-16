"""
Afternoon — Session 4 · 50 minutes · Code
dot_product.py — now using functions you learned yesterday
Create a new file:
dot_product.py
Today you can use
def
— you learned functions yesterday
"""

def dot_product(a,b) :
    result = 0 
    for i in range(len(a)) :
        result+= a[i]*b[i]
    return result

a = [1,2,]
b = [3,4]

print(f"{dot_product(a,b)}")