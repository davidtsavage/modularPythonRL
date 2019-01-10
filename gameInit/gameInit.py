import pygame
#data files
from constants import constants as c
from map.createMap import createMap
def gameInit():
    pygame.init()
    mS = pygame.display.set_mode((c.MSD['WIDTH'],
    	                          c.MSD['HEIGHT']))
    gM = createMap()
    return mS, gM