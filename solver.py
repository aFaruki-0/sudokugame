import requests
import numpy as np
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid=np.array(response.json()['board'])
empties = grid==0
solved=grid.copy()
for i in range(9):
    for j in range(9):
        if empties[i,j]==True:
            for a in range(9):
                if a+1==grid[i,a] and a+1==grid[a,j]:
                    continue
                else:
                    solved[i,j]=a+1
print(grid)
print(solved)
