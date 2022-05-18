import pygame
import time
import requests

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
pygame.init()
Width = 540
Height = 580
title = "Sudoku Game"
color = (239, 234, 216)
running = True
start = time.time()
numsPos = []
myfont = pygame.font.SysFont('Comic Sans MS', 35)
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption(title)
window.fill(color),
key= None

def drawTimer(gameTime, font):
    timer= font.render(f"Time: {gameTime}",True, (0,0,0))
    window.blit(timer, (350, 500))

def drawKey(font):
    showKey = font.render(f"Key: {key}", True, (0,0,0))
    window.blit(showKey, (50, 500))
def decideNumsPos(numsPos):
    for i in range(9):
        for a in range(9):
            numsPos.append([48*(i+1), 48*(a+1)])
def board():
    for i in range(9):
        for a in range(9):
            pygame.draw.rect(window, (0,0,0),[48*(i+1), 48*(a+1), 50, 50],2)

def drawNums(grid, numsPos, font):
    a=-1
    for b in range(9):
            for i in grid[b]:
                if i == 0 :
                    a +=1
                    continue
                else:
                    a +=1
                    num = font.render(f"{i}",True,(0,0,0))
                    window.blit(num, (numsPos[a][0], numsPos[a][1]))
def redraw_window(gameTime, font, numsPos, grid):
    window.fill(color)
    board()
    decideNumsPos(numsPos)
    drawKey(font)
    drawTimer(gameTime, font)
    drawNums(grid, numsPos, font)
while running:
    gameTime = round(time.time()-start)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_ESCAPE:
                    key=None

    mouse = pygame.mouse.get_pos()
    redraw_window(gameTime, myfont, numsPos, grid)
    pygame.display.update()
