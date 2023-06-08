import pygame
from load_image import *
from load_music import *
from projectile import *
from load_map import *


#Tạo đối tượng nhân vật
class player(object):
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.last_dash_time = 0
        self.dash_time = 500 
        self.isJump = False
        self.isDash = False
        self.isFalling = True
        self.left = False
        self.right = True
        self.walkCount = 0
        self.jumpCount = 9
        self.standing = True
        self.isAttack = False
        self.isAttacking = False
        self.attack_count = 0
        self.current_time = 0
        self.last_attack_time = 0
        self.attack_interval = 150
        self.hitbox = (self.x + 6 , self.y , 29, 52)
        self.prev_action = "right"
        self.now_action = "right"
        self.melee = AttackMelee(self.x,self.y)
        self.gravity = (self.jumpCount ** 2) * 0.5 * 1
    def get_prev_action(self):
        return self.prev_action
    
    def set_now_action(self):
        if self.left:
            self.now_action = "left"
        elif self.right:
            self.now_action = "right"
        
    def set_prev_action(self):
        self.prev_action = self.now_action
    
    def draw(self, win):
        self.draw_move(win)
        
        self.draw_jump(win)
        
        self.draw_attack(win)
    
    def draw_move(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left and not self.isJump and not self.isDash:
                win.blit(walkLeft[self.walkCount%3], (self.x,self.y))
                self.walkCount += 1
            elif self.right and not self.isJump and not self.isDash:
                win.blit(walkRight[self.walkCount%3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right and not self.isJump and not self.isDash:
                win.blit(walkRight[1], (self.x, self.y))
            elif self.left and not self.isJump and not self.isDash:
                win.blit(walkLeft[1], (self.x, self.y))
    
    def draw_jump(self,win):
        if self.isJump and self.left :
            win.blit(jumpleft,(self.x,self.y)) 
        elif self.isJump and self.right :
            win.blit(jumpright,(self.x,self.y))
        elif self.isJump:
            if self.prev_action == "left":
                win.blit(jumpleft,(self.x,self.y))
            elif self.prev_action == "right":
                win.blit(jumpright,(self.x,self.y))
        elif not self.isJump and not self.left and not self.right:
            if self.prev_action == "left":
                win.blit(walkLeft[1], (self.x, self.y))
            elif self.prev_action == "right":
                win.blit(walkRight[1], (self.x, self.y))     
        self.hitbox = (self.x + 6 , self.y , 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    
    def draw_attack(self, win):
        self.melee = AttackMelee(self.x,self.y)
        if self.attack_count >= 3:
            self.attack_count = 0
        if self.isAttack and self.prev_action == "left":
                self.current_time = pygame.time.get_ticks()
                time_elapsed = self.current_time - self.last_attack_time
                if time_elapsed > self.attack_interval :
                    self.melee.drawL(win,self.attack_count%3)
                    self.attack_count += 1
                    self.last_attack_time = self.current_time
                
        elif self.isAttack and self.prev_action == "right":
                self.current_time = pygame.time.get_ticks()
                time_elapsed = self.current_time - self.last_attack_time
                if time_elapsed > self.attack_interval  :
                    self.melee.drawR(win,self.attack_count%3)
                    self.attack_count += 1
                    self.last_attack_time = self.current_time
           
    def move(self, keys):
        self.handle_move(keys)
        
        self.handle_jump(keys)
        
        self.handle_dash(keys)
        
        self.handle_attack(keys)

    def handle_move(self,keys):
        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.right = False
            self.left = True
            self.standing = False
            self.set_prev_action()
            self.set_now_action()
        elif keys[pygame.K_RIGHT] and self.x < 1080 - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
            self.standing = False
            self.set_prev_action()
            self.set_now_action()
        else:
            self.standing = True
            self.walkCount = 0
    
    def handle_jump(self,keys):
        
        if not(self.isJump ) :
            if keys[pygame.K_x]:
                channel_move.play(jump_sound)
                self.isJump = True
                self.right = False
                self.left = False
                self.walkCount = 0

                
        else:
            if self.jumpCount >= -9:
                neg = 1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                if self.jumpCount < 0:
                    self.isJump = False
                    self.isFalling = True

                self.jumpCount -= 1
    
            else:
                self.isFalling = False
                self.isJump = False
                self.standing = True
                self.jumpCount = 9
                
                

        

    def handle_dash(self,keys):    
        if not(self.isDash):
            if keys[pygame.K_z]:
                channel_move.play(dash_sound)
                self.isDash = True
                self.vel += 40
        else:
            self.isDash = False
            self.vel = 10
     
    def handle_attack(self,keys):
        if keys[pygame.K_c]:
            channel_move.play(attack_sound)
            self.isAttack = True
                      
        else:
            self.isAttack = False
  
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
                            self.jumpCount = 9
                            self.y = tile_y - self.height + 15 
                            return

            self.y += self.gravity




