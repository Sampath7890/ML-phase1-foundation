"""Create two lists:
items = ["Rice", "Dal", "Oil", "Sugar", "Tea"]
prices = [50, 80, 120, 45, 60]

Loop through both together and print:
Item: Rice — ₹50
Item: Dal  — ₹80
...
Total bill: ₹355
Hint: use range(len(items)) to index both lists"""

items = ["Rice", "Dal", "Oil", "Sugar", "Tea"]
prices = [50, 80, 120, 45, 60]
total = 0

for i in range(len(items)) :
    print(f"Item : {items[i]} - ₹{prices[i]}")
    total+=prices[i]
print(f"Total bill: ₹{total}")    
