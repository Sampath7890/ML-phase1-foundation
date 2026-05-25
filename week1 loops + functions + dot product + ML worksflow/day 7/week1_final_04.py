#Write get_grade(average) that returns grade letter

# Function to return grade letter

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


average = int(input("enter average :"))

grade = get_grade(average)

print("Grade =", grade)