import pygame
from load_image import *

class AttackMelee(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hitbox = (self.x ,self.y , 70, 70 )
    def drawL(self,win, index):
        win.blit(attackL[index], (self.x - 80, self.y -20))
        self.hitbox = (self.x - 65 ,self.y - 8, 70, 70 )
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        
    def drawR(self,win, index):
        win.blit(attackR[index], (self.x + 20, self.y-20))
        self.hitbox = (self.x +35 ,self.y - 8, 70, 70 )
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)