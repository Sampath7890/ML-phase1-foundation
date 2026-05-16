"""
Take a 2D vector as input.
Print which quadrant it lives in:
- x>0, y>0 → "Quadrant 1 — top right"
- x<0, y>0 → "Quadrant 2 — top left"
- x<0, y<0 → "Quadrant 3 — bottom left"
- x>0, y<0 → "Quadrant 4 — bottom right"
- x=0, y=0 → "Origin — zero vector"
"""

x = int(input("enter vector v1 x: "))
y = int(input("enter vector v1 y: "))
print(f"vector = [{x},{y}]")

if x > 0 and y > 0 :
    print("Quadrant 1 — top right")
elif x<0 and y>0 :
    print("Quadrant 2 — top left")  
elif x<0 and y<0 :
    print("Quadrant 3 — bottom left") 
elif x>0 and y<0 :
    print("Quadrant 4 — bottom right")
else :
    print("Origin — zero vector")           
