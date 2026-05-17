"""
Create a list of 4 KMCE students, each with marks in 3 subjects as a vector"""

students = [
    {"name" : "ram" , "marks"  : [80,70,65]} ,
    {"name" : "sam" , "marks"  : [80,70,65]} , 
    {"name" : "sita" , "marks"  : [80,70,65]} ,
    {"name" : "laxmaj" , "marks"  : [80,70,65]}
]

for student in students :
    print(f"name = {student['name']} nd marks = {student['marks']}")