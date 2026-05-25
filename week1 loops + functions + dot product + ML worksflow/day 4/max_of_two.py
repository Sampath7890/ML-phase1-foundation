"""
Write get_max(a, b) that returns the larger number
Without using Python's built-in max().
get_max(10, 20) → 20, get_max(7, 3) → 7, get_max(5, 5) → 5
"""

def get_max(x,y) :
    if x > y :
     return x
    else :
       return y

x = int(input("enter a number x: "))
y = int(input("enter a number y: "))
 
print(f"larger num is {get_max(x,y)}")