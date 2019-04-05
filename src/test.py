# coding=utf-8
import pygame
pygame.init()

ourScreen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('mygame')
finish = False
colorBlue = True

# game loop
while not finish:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        colorBlue = not colorBlue
    if colorBlue:
        color = (0, 128, 255)
    else:
        color = (255, 255, 255)
    # Draw Screen
    pygame.draw.rect(ourScreen, color, pygame.Rect(0, 0, 60, 60))
    # Update Game State
    pygame.display.flip()
pygame.quit()
