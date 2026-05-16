"""
A cab charges ₹50 for the first 2 km and ₹12 per km after that. Take distance as input. Calculate and print the total fare
"""

distance = int(input("enter how many kilometers: "))

if distance <=2 :
    fare = 50
else :
   fare= (distance - 2 ) * 12

print(f"fare for {distance} kilometers will be {fare}")