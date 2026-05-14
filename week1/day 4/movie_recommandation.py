"""Movies have one feature only — rating out of 10.
movies = ["RRR", "KGF", "Pushpa", "Baahubali"]
ratings = [9.2, 8.8, 8.1, 9.5]

Write get_best_movie(movies, ratings) that:
→ loops through both lists
→ finds the movie with highest rating
→ returns its name

Print: "Best movie: Baahubali"
"""
def get_best_movie(movies , ratings) :
    highest_rating = ratings[0]
    best_movie = movies[0]
    
    for i in range(len(ratings)) :
        if ratings[i] > highest_rating :
            highest_rating=ratings[i]
            best_movie=movies[i]
    return best_movie        


movies = ["RRR", "KGF", "Pushpa", "Baahubali"]
ratings = [9.2, 8.8, 8.1, 9.5]

print(f"best movie = {get_best_movie(movies , ratings)}")