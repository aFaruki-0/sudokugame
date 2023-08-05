import random
grid =[[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]
board=grid
nums=[1,2,3,4,5,6,7,8,9]
def generate():
    find = find_empty()
    if not find:
        return True
    else:
        row, col = find

    for y in range(9):
        i=random.choice(nums)
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if generate():
                return True

            grid[row][col] = 0

    return False
def makeEmptyCell():
    for i in range(50):
        x = random.randrange(9)
        y = random.randrange(9)
        grid[x][y]=0

def valid(grid, num, pos):
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
    boxX = pos[1] // 3
    boxY = pos[0] // 3
    for i in range(boxY*3, boxY*3 + 3):
        for j in range(boxX * 3, boxX*3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True


def printGrid():
    for i in grid:
        print(i)
    print('------------------------------------')


def find_empty():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)

    return None