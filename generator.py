import random
grid=[[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]
nums=[1,2,3,4,5,6,7,8,9],
def checkCol(grid,row,col,num):
    if num in grid[col]:
        return False
    else:
        return True
    
def checkRow(grid,row,col,num):
    for i in range(9):
        if num == grid[row][i]:
            return False
    else:
        return True
def creator(grid,nums):
    for col in range(9):
        for row in range(9):
            num=random.choice(nums)
            if checkCol(grid,row,col,num) and checkRow(grid,row,col,num):
                grid[col][row]=num
creator(grid,nums)
for i in range(9):
    print(grid[i])