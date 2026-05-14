"""Write get_grade(marks) that returns grade letter
90+ → "A", 75-89 → "B", 60-74 → "C", 40-59 → "D", below 40 → "F"
Test with at least 6 different marks."""

def get_grade(marks) :
    if marks >= 90 :
        return "A"
    elif marks >=75 :
        return "B"
    elif marks >= 60 :
        return "C"
    elif marks >= 40 :
        return "D" 
    else :
        return "FAIL better luck next time"

marks = int(input("enter how many marks do uh got : "))
print(f"marks = {marks} and you got {get_grade(marks)}")



                                                                        