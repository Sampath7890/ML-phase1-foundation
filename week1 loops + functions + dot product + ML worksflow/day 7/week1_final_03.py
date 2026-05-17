"""Write find_similar(target, students, names) that finds the most similar student
"""

def dot_product(a,b) :
    result = 0
    for i in range(len(a)) :
        result += a[i] * b[i]
    return result

def find_similar(target, students, names) :
    best_score = -1
    best_student = ""
    for i in range(len(students)):
        score = dot_product(target , students[i])
        print(f"{names[i]} similar students = {score}")
        if score > best_score :
            best_score = score
            best_student = names[i]
    return best_student

names = ["Rahul", "Sneha", "Arjun", "Priya"]

students = [
    [85, 90, 88],   # Rahul
    [78, 82, 80],   # Sneha
    [92, 95, 91],   # Arjun
    [70, 75, 72]    # Priya
]
target = [80, 85, 84]


answer = find_similar(target, students, names)

print("\nMost similar student is:", answer)
           


