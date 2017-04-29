__author__ = 'ankush'
import pygame
import random
import time
import numpy as np

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.key.set_repeat(1,30)

def gameBegin():
    global s_len,exitGame,s_h,s_w,s_x,s_y,f_h,f_w,flag,score,f_x,f_y,s_co,dx,dy,lastKey,fps
    gameDisplay.fill((0,255,0))
    pygame.display.set_caption('snakes')
    exitGame = False
    fps = pygame.time.Clock()
    s_x,s_y = (400,300)
    s_h,s_w = (20,20)
    f_h = 20
    f_w = 20
    flag = 0
    score  = 0
    f_x,f_y = (random.randrange(0,800,20),random.randrange(0,600,20))
    pygame.display.update()
    s_co = []
    s_len = 10
    dx = 0
    dy = 0
    lastKey = pygame.K_0
    gameLoop()

def drawSnake(s_co,s_si):
    s_h,s_w = s_si
    for (s_x,s_y) in s_co:
     pygame.draw.rect(gameDisplay,(150,0,150),[s_x,s_y,s_h,s_w])


def gameOver():
    gameDisplay.fill((0,255,0))
    pygame.display.flip()
    global s_len,exitGame,s_h,s_w,s_x,s_y,f_h,f_w,flag,score,f_x,f_y,s_co,dx,dy,lastKey,fps
    font = pygame.font.SysFont(None,25)
    txt = font.render("Game Over!",True,(0,0,0))
    gameDisplay.blit(txt,[400,400])
    pygame.display.flip()
    pygame.time.delay(2000)
    exitGame = True
def gameLoop():
    global s_len,exitGame,s_h,s_w,s_x,s_y,f_h,f_w,flag,score,f_x,f_y,s_co,dx,dy,lastKey,fps
    while not exitGame:
        if np.abs(s_x-f_x)==0 and np.abs(s_y - f_y)==0:
            flag = 1
            f_x,f_y = (random.randrange(0,800,20),random.randrange(0,600,20))
            gameDisplay.fill((0,0,0),rect=[f_x,f_y,f_h,f_w])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_press = event.key
                if key_press == pygame.K_UP:
                    if lastKey == 274:
                        dy = 0
                        dx = 20
                    else:
                        dy = -20
                        dx = 0
                elif key_press == pygame.K_DOWN:
                    if lastKey == 273:
                        dy = 0
                        dx = 20
                    else:
                        dy = 20
                        dx = 0
                elif key_press == pygame.K_LEFT:
                    if lastKey == 275:
                        dy = -20
                        dx = 0
                    else:
                        dx = -20
                        dy = 0
                elif key_press ==pygame.K_RIGHT:
                    if lastKey == 276:
                        dy = -20
                        dx = 0
                    else:
                        dx = 20
                        dy = 0
                if key_press == pygame.K_ESCAPE:
                    exitGame = True
                lastKey = key_press
        if (s_x <= 0) or (s_x>= 800) or (s_y <= 0) or (s_y >= 600):
            gameOver()
        s_x += dx
        s_y += dy
        gameDisplay.fill((0,255,0))
        if flag == 1:
            score += 1
            s_len += 2
            flag = 0
        s_head = (s_x,s_y)
        if len(s_co)>s_len:
            del s_co[0]
        if s_head != (400,300) and s_head in s_co[:-5]:
            font = pygame.font.SysFont(None,25)
            txt = font.render("u crashed .. game over!",True,(255,0,0))
            gameDisplay.blit(txt,[400,300])
            pygame.display.update()
            time.sleep(2)
            exitGame = True
        s_co.append(s_head)
        s_si = (s_h,s_w)
        drawSnake(s_co,s_si)
        gameDisplay.fill((255,0,0),rect=[f_x,f_y,f_h,f_w])
        fps.tick(60)
        font = pygame.font.SysFont(None,40)
        stxt = font.render("score : %s"%(score),True,(255,255,255))
        gameDisplay.blit(stxt,[650,0])
        pygame.display.update()
    pygame.quit()

gameBegin()

quit()
