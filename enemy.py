import pygame
from load_image import *
from load_music import *
from projectile import *


class Enemy(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.ishitted = False

        self.vel = 2
        self.hitbox = (self.x , self.y + 2, 20, 30)
        self.health = 10
        self.visible = True
        self.current_time = 0
        self.last_hitted = 0
        self.hitted_duration = 200
        self.action = "right"
    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.action == "right":
                
                    win.blit(walkRightE1[self.walkCount %3], (self.x, self.y))
                    self.walkCount += 1
            elif self.action == "left":
                
                    win.blit(walkLeftE1[self.walkCount %3], (self.x, self.y))
                    self.walkCount += 1
    
                
            
            
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x +5, self.y + 2, 31, 50)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            
            if self.ishitted:
                self.vel = 0
            else:
                self.vel = 2
                
    def update(self):
        self.move()
                
        

    def move(self):
        
        if self.action == "right":
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.action = "left"
                self.walkCount = 0
        elif self.action == "left":
            if self.x - self.vel > self.path[0]:
                    self.x -= self.vel
            else:
                self.action ="right"
                self.walkCount = 0
        
    def hit(self):
        self.ishitted = True
        if self.ishitted:
            if self.action == 'right' :
                    self.action = 'left'
            elif self.action == 'left':
                    self.action ='right'
        if self.health > 0:
            self.health -=0.5    
        else:
            self.visible = False
        
        print('hit')