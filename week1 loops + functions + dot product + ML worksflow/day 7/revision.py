# 1. Variables — write all 4 types
name = "sampath"
age = 20
gpa = 6.5
is_student = True

# 2. F-string — introduce yourself
print(f"my name is {name} and iam {age} year's old.")

# 3. For loop — print 1 to 10
for i in range(10):
    print(i)

# 4. While loop — count down from 5 to 1
n = 5
while n > 0:
    print(n)
    n -= 1

# 5. List — your 5 subjects at KMCE
subjects = ["maths" , "dbms" , "atcd" ,"coa", "pps"]
for sub in subjects:
    print(sub)

# 6. Function — takes marks, returns grade
def get_grade(marks):
    if marks>= 90:
        return "A"
    elif marks >= 80:
        return "B"
    else:
        return "C"

# 7. dot_product — from memory
def dot_product(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result