"""
Take a student's mark as input (out of 100). Print their grade:

90 and above → A
75 – 89 → B
60–74 → C
40–59 → D
Below 40 → Fail
"""

marks = int(input("student marks out of 100: "))
if(marks>=90) :
    print("the grade is A")
elif(marks>=75) :
    print("the grade is B")
elif(marks>=60) :
    print("the grade is C")
elif(marks>=40) :
    print("the grade is D")
else: 
    print("fail")              