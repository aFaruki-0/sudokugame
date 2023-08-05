from random import randrange
def printGrid(board):
    for i in range(50):
        x = randrange(9)
        y = randrange(9)
        board[x][y]=0
def solve(board):
    findEmpty = emptyCell(board)
    
    if not findEmpty:
        return True
    else:
        row, column = findEmpty
    
    for i in range(1,10):
        if isValid(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True

        board[row][column] = 0
    return False
def isValid (board, num, pos):
    for i in range(9):
        if num == board[pos[0]][i]:
            return False
    for i in range(9):
        if num == board[i][pos[1]]:
            return False

    row = pos[0] // 3 
    column = pos[1] // 3 

    for i in range(row * 3, (row * 3) + 3):
        for j in range(column * 3, (column * 3) + 3):
            if num == board[i][j]:
                return False 
    return True
def emptyCell(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return (row,column)
    return None
