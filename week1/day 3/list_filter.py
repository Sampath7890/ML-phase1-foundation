"""Filter passing marks
Create a list of 8 marks (mix of passing and failing).
Loop through and print only marks above 40 (passing).
Also count how many passed and how many failed."""

marks = {40,60,90,20,88,100,10,50}
passed = 0
failed = 0
for i in marks :
    if i <= 40 :
        print(f"{i}.passed")
        passed+=1
    else:
        print(f"{i}.failed")
        failed+=1
print("passed",passed)
print("failed",failed)         