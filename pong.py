__author__ = 'ankush'
import pygame,sys
from pygame.locals import *

#set fps of game
FPS = 200
#set window height and width
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

def run():
    ## initialize pygame and declare global display area
    pygame.init()
    global DISPLAYSURFACE

    ## set display
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURFACE = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Pong')

    ## main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


run()
