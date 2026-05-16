"""
Take 3 subject marks as input. Calculate the average. Print the average
 and whether the student passed (average ≥ 50) or failed.
"""
python = int(input("enter your python marks: "))
ai = int(input("enter your ai marks: "))
java =int(input("enter your java marks: "))

average = python + ai +java / 3

if(average >= 50) :
    print(f"your average is {average} and you are pass")
else:
    print(f"your average is {average} and you are fail")
