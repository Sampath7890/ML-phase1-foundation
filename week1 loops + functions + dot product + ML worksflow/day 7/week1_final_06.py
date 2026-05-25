#Print who is most similar to student 1

students = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 91],
    [70, 75, 72]
]

def dot_product(v1,v2) :
    total = 0
    for i in range(len(v1)) :
        total += v1[i]* v2[i]
    return total

    
target = 0 

best_score = -1
most_similar = -1


for i in range(len(students)) :
    if i != target :
        score = dot_product(students[target] , students[i]) 
        print(f"student {target} vs student {i}={score}")

        if score > best_score :
            best_score =score
            most_similar = i
print((f"most similar to student {target} is {most_similar}"))
                 