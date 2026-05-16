"""Write a full restaurant recommender:

your_orders = [8, 1, 6, 2]  
(biryani, pizza, dosa, burger — times ordered)

restaurants = [
    [9, 0, 7, 1],   # Bawarchi
    [1, 8, 0, 9],   # Pizza Hut
    [7, 0, 9, 0],   # Chutneys
    [0, 7, 0, 8]    # Burger King
]
names = ["Bawarchi", "Pizza Hut", "Chutneys", "Burger King"]

Print each restaurant's similarity score.
Print the top recommendation.
Also print: "Not recommended:" and list the lowest scoring one."""


import math

your_orders = [8, 1, 6, 2]  


restaurants = [
    [9, 0, 7, 1],   # Bawarchi
    [1, 8, 0, 9],   # Pizza Hut
    [7, 0, 9, 0],   # Chutneys
    [0, 7, 0, 8]    # Burger King
]
names = ["Bawarchi", "Pizza Hut", "Chutneys", "Burger King"]


def dot_product(a,b):
    result = 0 
    for i in range(len(a)) :
        result += a[i]*b[i]
    return result

def magnitude(v) :
    total = 0
    for num in v :
        total += num * num 
    return math.sqrt(total)

def cosine_similarity(a,b) :
    dot = dot_product(a,b)
    mag_a =magnitude(a)
    mag_b = magnitude(b)

    if mag_a == 0 or mag_b == 0 :
        return 0
    
    return dot / (mag_a * mag_b)

scores = []

print("====resturaent similarity score====")

for i in range(len(restaurants)) :
    score = cosine_similarity(your_orders , restaurants[i])
    scores.append(score)
    print(f"{names[i]} = {score:.2f}")


best_score = max(scores)
best_index = scores.index(best_score)

print("==== top recommended ====")

print(f"{names[best_index]}")


worst_score = min(scores)
worst_index = scores.index(worst_score)

print("===== worst recommandation =====")
print(names[worst_index])

