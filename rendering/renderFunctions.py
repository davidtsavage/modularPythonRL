import pygame
from constants import constants as c

def renderGame(mainSurface,gameMap):
    mainSurface.fill(c.COL['BLACK'])
    renderMap(gameMap,mainSurface)
    mainSurface.blit(c.SPR['1-255,255,255-0-10x10'],(10,10))
    pygame.display.flip()

def renderMap(mapToRender,surface):
    for x in range(0,c.MAPD['WIDTH']):
        for y in range(0,c.MAPD['HEIGHT']):
            if mapToRender[x][y].blocksPath == True:
                if mapToRender[x][y].blocksSight == True:
                    surface.blit(c.SPR['2-255,255,255-0-10x10'],(x*c.TD['WIDTH'],y*c.TD['HEIGHT']))