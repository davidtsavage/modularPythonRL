from constants import constants as c
from tile.tile import Tile
def createMap():
    newMap = [[ Tile(False,False) for y in range(0,c.MAPD['WIDTH'])] for y in range(0,c.MAPD['HEIGHT'])]
    newMap[10][10].blocksPath = True
    newMap[10][10].blocksSight = True
    newMap[10][15].blocksPath = True
    newMap[10][15].blocksSight = True
    return newMap