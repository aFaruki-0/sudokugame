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
def printGrid():
    for i in grid:
        print(i)
    print('------------------------------------')
def checkEmpty():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return True
    return False
def checkCellEmpty(row, col):
    if grid[row][col]==0:
        return True
    return False
def checkRowEmpty(row):
    for i in range(9):
        if grid[row][i]==0:
            return True
    return False
def makeBoard():
    nums=[1,2,3,4,5,6,7,8,9]
    while checkEmpty():
        for i in range(9):
            for j in range(9):
                printGrid()
                if checkCellEmpty(i,j):
                    num=random.choice(nums)
                    if isValid(num,i,j):
                        grid[i][j]=num
                    if checkRowEmpty(i):
                        makeBoard()

        printGrid()

                   
def isValid (num,row,col):
    for i in range(9):
        if num == grid[row][i]:
            return False
    for i in range(9):
        if num == grid[i][col]:
            return False

    # row = row1 // 3 
    # column = col1 // 3 

    # for i in range(row * 3, (row * 3) + 3):
    #     for j in range(column * 3, (column * 3) + 3):
    #         if num == board[i][j]:
    #             return False 
    return True
makeBoard()
printGrid()
