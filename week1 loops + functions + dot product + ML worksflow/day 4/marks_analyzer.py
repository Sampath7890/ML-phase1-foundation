"""
Write 4 functions for a marks list
get_average(marks) → returns average
get_highest(marks) → returns highest mark
get_lowest(marks) → returns lowest mark
count_passed(marks, passing=40) → returns how many passed

Test with: [78, 35, 92, 28, 65, 88, 15, 72, 45, 60]
"""

def get_average(marks):
    total = 0
    for mark in marks :
        total += mark
    return total / len(marks)

def get_highest(marks) :
    highest = marks[0]
    for mark in marks :
        if mark > highest :
            highest = mark
    return highest

def get_lowest(marks) :
    lowest = marks[0]
    for mark in marks :
        if mark < lowest :
            lowest = mark
    return lowest

def count_passed(marks, passed=40):
    count = 0 
    for mark in marks :
        if mark >= passed :
            count+=1
    return count

marks = [78, 35, 92, 28, 65, 88, 15, 72, 45, 60]

print(f"average = {get_average(marks)}")
print(f"highest = {get_highest(marks)}")
print(f"lowest = {get_lowest(marks)}")
print(f"passed count = {count_passed(marks)}")