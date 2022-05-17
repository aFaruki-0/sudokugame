import pygame

pygame.init()
Width = 540
Height = 540
title = "Sudoku Game"
color = (14, 19, 175)
running = True


window = pygame.display.set_mode((Width, Height), pygame.RESIZABLE)
pygame.display.set_caption(title)


  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(color)
    pygame.display.flip()
    pygame.display.update()
