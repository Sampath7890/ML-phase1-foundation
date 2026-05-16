def dot_product(a,b) :
    result = 0
    for i in range(len(a)) :
        result += a[i] * b[i]
    return result

def similar_students(target , student , names) :
    best_score = -1
    most_similar = ""
    for i in range(len(student)) :
        score = dot_product(target , student[i])
        if score > best_score :
            best_score = score 
            most_similar = names[i]
    return most_similar

sampath = [85, 90, 78]
classmates = [[88,91,80], [50,45,60], [84,88,75]]
c_names = ["Ram", "sita", "laxman"]

similar = similar_students(sampath , classmates , c_names)

print(f"similar student = {similar}")
