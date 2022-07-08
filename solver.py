import requests
import numpy as np
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid=np.array(response.json()['board'])
empties = grid==0
for i in range(9):
    for j in range(9):
        if empties[i,j]==True:
            pass