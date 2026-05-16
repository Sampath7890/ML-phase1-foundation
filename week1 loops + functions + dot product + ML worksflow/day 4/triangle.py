"""P8 —  Medium
Write is_valid_triangle(a, b, c) and triangle_type(a, b, c)
is_valid_triangle: returns True if valid (sum of any 2 sides > third)
triangle_type: returns "Equilateral", "Isoceles", or "Scalene"
triangle_type should FIRST call is_valid_triangle — if not valid, return "Not a triangle" """

def is_valid_triangle(a, b, c) :
    return (a + b > c) and (b + c > a) and (a + c > b)
def triangle_type(a, b, c) :
    if not is_valid_triangle(a, b, c) :
        return "not a valid traingle"
    elif a==b==c :
        return "equalaterial Traingle"
    elif a==b or b==a or c==a :
        return "Iscoceles Traingle"
    else :
        return "scalane Traingle"

a = int(input("enter a side of a traingle(a): "))    
b = int(input("enter a side of a traingle(b): ")) 
c = int(input("enter a side of a traingle(c): "))    

print(f"{triangle_type(a,b,c)}")