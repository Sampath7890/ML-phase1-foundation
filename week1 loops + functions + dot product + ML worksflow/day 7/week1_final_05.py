#Loop through all students — print each one's average and grade


def get_grade(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"


# Student data
names = ["Rahul", "Sneha", "Arjun", "Priya"]

students = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 91],
    [70, 75, 72]
]

for i in range(len(students)) :
    marks = students[i]
    average = sum(marks) / len(marks)
    grade = get_grade(average)
    print(f"name = {names[i]} \n  average = {average} \n grade = {get_grade(average)}")