"""Write a function calculate_grade(marks, total=100) using a default parameter.
Calculate percentage and return "A", "B", "C" or "Fail" based on marks.
Call the function using different inputs and print the grades.
"""
def calculate_grade(marks, total = 100) :
    percentage = (marks/total)*100
    if percentage >= 99 :
        return "A+"
    elif percentage >= 85 :
        return "A"
    elif percentage >= 75 :
        return "B+"
    elif percentage >= 60 :
        return "C"
    else:
        return "Fail"
name = input("enter your name: ")   
marks = int(input("enter you marks: "))
print(f"grade of {name} with {marks} = ",calculate_grade(marks))