import pygame
from rendering.renderFunctions import renderGame
def gameMainLoop(mainSurface,gameMap):
    gameQuit = False
    while not gameQuit:
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                gameQuit = True
        renderGame(mainSurface, gameMap)
    pygame.quit()
    exit()