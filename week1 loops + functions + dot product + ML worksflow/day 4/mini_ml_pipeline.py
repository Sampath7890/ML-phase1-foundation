"""Your first mini ML data pipeline
This combines EVERYTHING you've learned so far.

Write these functions:
load_data() → returns a list of student dicts with name and marks
get_average(marks) → average of a list
classify_student(avg) → "Distinction/First/Second/Pass/Fail"
process_students(students) → loops through all, computes avg, classifies each
print_report(results) → prints formatted output

Call them all in sequence. This is a real data pipeline.
This is exactly how ML preprocessing pipelines work — load data → process each row → classify → report"""

def load_data() :
    students = [
        {"name" : "ram" , "marks": [89, 90, 95]},
        {"name" : "sam" , "marks" : [85 , 75 ,85 ]},
        {"name" : "sita" , "marks" : [75, 75,65]},
        {"name" : "laxman" , "marks" : [40 ,50, 30]}
    ]

    return students

def get_average(marks) :
    total = sum(marks)
    average = total / len(marks)

    return average

def classify_students(average):
    if average >= 75 :
        return "distinction"
    elif average >= 65 :
        return "first class"
    elif average >= 55 :
        return "second class"
    elif average >= 45 : 
        return "pass"
    else :
        return "fail" 
    
def process_students(students) :
    results = []
    for student in students :
        avg = get_average(student["marks"])
        classification = classify_students(avg)
        result = {
            "name" : student["name"],
            "average" : avg ,
            "classification" : classify_students(avg)
        }
        results.append(result)
    return results


def print_report(results) :
    print("=======student report=========")

    for student in results :
        print()
        print(f"name                  : {student['name']}")
        print(f"average               : {student['average']}")
        print(f"classification        : {student['classification']}")
              


students = load_data()
results= process_students(students)
print_report(results)