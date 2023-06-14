import pygame
from load_image import *
from load_music import *
from projectile import *
from load_map import *

# Tạo đối tượng enemy
class Enemy(object):
    #Khởi tạo
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.ishitted = False
        self.jumpCount = 9
        self.isJump = False
        self.isFalling  = True
        self.gravity = (self.jumpCount ** 2) * 0.5 * 1
        self.vel = 2
        self.hitbox = (self.x , self.y + 5, 20, 30)
        self.health = 10
        self.visible = True
        self.current_time = 0
        self.last_hitted = 0
        self.hitted_duration = 200
        self.action = "right"
    #Vẽ enemy
    def draw(self,win,map):
        self.move()
        self.apply_gravity(map)
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.action == "right":
                
                    win.blit(walkRightE1[self.walkCount %3], (self.x, self.y))
                    self.walkCount += 1
            elif self.action == "left":
                
                    win.blit(walkLeftE1[self.walkCount %3], (self.x, self.y))
                    self.walkCount += 1
    
            
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x +5, self.y +10, 31, 35)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            
            if self.ishitted:
                self.vel = 0
            else:
                self.vel = 2
    #Chuyển động
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
    #Bị đánh 
    def hit(self):
        self.ishitted = True
        if self.ishitted:
            if self.action == 'right' :
                    self.action = 'left'
            elif self.action == 'left':
                    self.action ='right'
        if self.health > 0:
            self.health -=1   
        else:
            self.visible = False
    #Thêm trọng lực  
        
    def apply_gravity(self, map):
        level_data = map.get_level_data("Wall")
        
        if self.isJump:
            return 
        if self.isFalling:
            hitbox = self.hitbox

            for row in range(len(level_data)):  
                for col in range(len(level_data[row])):
                    if level_data[row][col] != 0:
                        tile_x = col * map.tmxdata.tilewidth
                        tile_y = row * map.tmxdata.tileheight
                        tile_rect = pygame.Rect(tile_x, tile_y- map.tmxdata.tileheight, map.tmxdata.tilewidth, map.tmxdata.tileheight)
                        if tile_rect.colliderect(hitbox):
                            self.isJump = False  
                            self.isFalling = False
                            self.jumpCount = 9
                            self.y = tile_y - self.height - 15
                            return

            self.y += self.gravity
            
            
            
