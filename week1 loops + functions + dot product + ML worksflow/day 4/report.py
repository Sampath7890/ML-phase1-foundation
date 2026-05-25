"""Write these functions:
get_average(marks) → average
get_grade(average) → grade letter
is_promoted(average) → True if average >= 50
print_report(name, subjects, marks) → prints full formatted report

Call print_report with your own name, subjects, and marks."""

def get_average(marks) :
    total = sum(marks)
    average = total / len(marks)
    return average

def get_grade(average):
    if average >= 90 :
        return "A"
    elif average >= 75 :
        return "B"
    elif average >= 65 :
        return "C"
    elif average >= 55 :
        return "D"
    else :
        return "fail"
    
def is_promoted(average) :
    if average >= 50 :
        return "promoted"
    else :
        return "not promoted"
    
    
def print_report(name , subject , marks) :
    print("======student report===/====")
    print(f"name = {name}")
    print()

    average = get_average(marks)    

    print(f"average = {get_average(marks)}")
    print(f"grade = {get_grade(average)}")
    print(f"promoted = {is_promoted(average)}")

name = input("Enter your name: ")

subjects = ["Maths", "Physics", "Python", "English"]
marks = [85, 78, 92, 74]

print_report(name, subjects, marks)
