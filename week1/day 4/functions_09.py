def passing(mark) :
    return mark >= 40

class_marks =[40,50,45,36,80,99,100,40,50,78]
pass_count = 0
fail_count = 0

for mark in class_marks:
    if passing(mark) :
        print(f"{mark}= pass")
        pass_count+=1
    else :
        print(f"{mark}=fail")
        fail_count+=1
print(f"passing members = {pass_count}")
print(f"failing count = {fail_count}")   