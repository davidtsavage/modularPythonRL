from constants import constants as c
from gameInit.gameInit import gameInit
from gameLoops.gameMainLoop import gameMainLoop

if __name__ == '__main__':
    mSgM = gameInit()
    gameMainLoop(mSgM[0],mSgM[1])