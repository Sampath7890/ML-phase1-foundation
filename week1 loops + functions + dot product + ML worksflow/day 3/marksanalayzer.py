"""
Create a list of your marks in 5 subjects.
Using a for loop, print each subject mark.
Also print: total, average, highest, lowest using sum(), max(), min(), len()
"""

marks = {
    "DBMS" : 49 ,
    "SE" : 50 ,
    "maths" : 60 ,
    "ATCD" : 60 ,
    "DM" : 49
}

for student in marks :
    print(marks[student])

total = sum(marks.values())
average = total / len(marks)
highest = max(marks.values())
lowest = min(marks.values())

print(f"total marks = {total}")
print(f"average = {average}")
print(f"highest marks = {highest}")
print(f"lowest marks = {lowest}")