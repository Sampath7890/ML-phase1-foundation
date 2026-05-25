def dot_product(a,b) :
    result = 0

    for i in range(len(a)) :
        result+=a[i] * b[i]
    return result 

def movie_reco(user , movies , names) :
    best_movies = ""
    best_score = -1
    for i in range(len(movies)) :
        score = dot_product(user , movies[i])
        print(f"{names[i]}= score {score}")
        if score > best_score :
            best_score = score
            best_movies = names[i]
    return best_movies

user = [9 ,5,8]
movies = [  
    [8,2,7],
    [2,9,1],
    [7,3,9],
    [1,8,2]
]        

names = ["RRR" , "bahuballi" , "Avengers" ,"Mcu"]

rec = movie_reco(user , movies , names) 

print(f"best movie = {rec}")
