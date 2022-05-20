import pygame
import time
import requests

def menu():
    pygame.init()
    Width = 540
    Height = 580
    title = "Sudoku Game"
    color = (239, 234, 216)
    running = True
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    window = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption(title)
    window.fill(color)
    def drawButtons(myfont, window):
        pygame.draw.rect(window, (81,74,74), (175,200,200,75),0)
        pygame.draw.rect(window, (0,0,0), (175,200,200,75),4)
        pygame.draw.rect(window, (81,74,74), (175,300,200,75),0)
        pygame.draw.rect(window, (0,0,0), (175,300,200,75),4)
        text1 = myfont.render("Başla", True, (0,0,0))
        text2 = myfont.render("Çıkış", True, (0,0,0))
        text3 = myfont.render("Sudoku Oyunu", True, (0,0,0))
        window.blit(text1, (225, 210))
        window.blit(text2, (225, 310))
        window.blit(text3, (168, 100))
    def checkMouse(mouse):
        if mouse[0] < 375 and mouse[0] > 175 and mouse[1] > 200 and mouse[1] < 275:
            pygame.draw.rect(window, (43,39,39), (175,200,200,75),0)
            pygame.draw.rect(window, (0,0,0), (175,200,200,75),4)
            text1 = myfont.render("Başla", True, (0,0,0))
            window.blit(text1, (225, 210))
        if mouse[0] < 375 and mouse[0] > 175 and mouse[1] > 300 and mouse[1] < 375:
            pygame.draw.rect(window, (43,39,39), (175,300,200,75),0)
            pygame.draw.rect(window, (0,0,0), (175,300,200,75),4)
            text2 = myfont.render("Çıkış", True, (0,0,0))
            window.blit(text2, (225, 310))      
    def redraw_window(myfont, window,mouse):
        window.fill(color)
        drawButtons(myfont, window)
        checkMouse(mouse)
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] < 375 and mouse[0] > 175 and mouse[1] > 200 and mouse[1] < 275:
                    game()
                    running=False
                if mouse[0] < 375 and mouse[0] > 175 and mouse[1] > 300 and mouse[1] < 375:
                    running=False
            redraw_window(myfont, window, mouse)
            pygame.display.update()

def game():
    response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
    defgrid = response.json()['board']
    grid = response.json()['board']
    pygame.init()
    Width = 540
    Height = 580
    title = "Sudoku Game"
    color = (239, 234, 216)
    running = True
    start = time.time()
    numsPos = []
    buttons = []
    emptySlots = []
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    window = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption(title)
    window.fill(color)
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
    def checkEmpty(grid,emptySlots):
        for i in range(9):
            for j in range(9):
                if grid[i][j]==0:
                    emptySlots.append([i, j])
    def clicked(mouse, key, buttons, font, grid, defgrid):
        a=-1
        for i in range(9):
            for j in range(9):
                a+=1
                if mouse[0] > buttons[a][0] and mouse[0] < buttons[a][1] and mouse[1] > buttons[a][2] and mouse[1] < buttons[a][3]:
                    if not defgrid[i][j]==0:
                        continue
                    else:
                        grid[i][j]=key
    def getButtonPos(buttons):
        for i in range(9):
            for a in range(9):
                buttons.append([48*(i+1), (48*(i+1))+48, 48*(a+1), (48*(a+1))+48])
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
    def redraw_window(gameTime, font, numsPos, grid, emptySlots, buttons):
        window.fill(color)
        board()
        getButtonPos(buttons)
        decideNumsPos(numsPos)
        drawKey(font)
        drawTimer(gameTime, font)
        drawNums(grid, numsPos, font)
        checkEmpty(grid, emptySlots)

    while running:
        gameTime = round(time.time()-start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                clicked(mouse, key, buttons, myfont, grid, defgrid)
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


        redraw_window(gameTime, myfont, numsPos, grid, emptySlots, buttons)
        pygame.display.update()

menu()