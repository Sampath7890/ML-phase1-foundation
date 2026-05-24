"""Dot product reborn
Redo your Week 1 movie recommender — but now using np.dot() instead of your manual function.
user = [9,1,8]
movies = [[8,2,7],[2,9,1],[7,3,9],[1,8,2]]
names = ["RRR","DDLJ","KGF","Kabir Singh"]
Find best movie using np.dot — no loops."""

import numpy as np 
user = np.array([9,1,8])
movies = np.array([[8,2,7],
                   [2,9,1],
                   [7,3,9],
                   [1,8,2]])
names = np.array(["RRR","DDLJ","KGF","Kabir Singh"])

score = np.dot(movies , user)
best_score = np.argmax(score)

print(f"best movie with index = {names[best_score]}")