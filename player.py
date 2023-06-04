import pygame


WIDTH, HEIGHT = 1080, 720
class Player:
    ACTIONS = {
        "normal":{
            "walk" : 
            "jump" :
 
            "stand":

        },

    }

    WALK_VEL = 5
    DASH_VEL = 40
    GRAVITY = 10
    JUMP_VEL = 0.2
    
    def __init__(self, x, y, direction, window_width = 0, window_height = 0) :
        self.x = x
        self.y = y
        self.window_width = window_width
        self.window_height = window_height
        self.direction = direction
        self.action = "walk"
        self.animation_count = 0
        self.frame_duration = 5
        self.img = None
        self.action_type = "weapon"
        self.vel = self.WALK_VEL
        self.jumping = False
        self.jump_count = 0
        self.jump_duration = 20
        self.set_image()
    
    def apply_gravity(self):
        if self.y + 128 <= self.window_height:
            self.y += self.GRAVITY
        elif self.jump_count == 0 and self.action == "falling":
            self.action = "stand"
    
    
    def set_image(self):
        action = self.ACTIONS[self.action_type][self.action][self.direction]
              
        if self.animation_count // self.frame_duration >= len(action[1]):
            self.animation_count = 0
            
            if self.jumping:
                self.action = "falling"
            
            if self.action_type == "attack":
                self.action_type = "weapon"
                self.action = "stand"
        
        self.img = [layer[self.animation_count//self.frame_duration]
                    for layer in action if layer]
        
    def draw(self,win):
        for layer in self.img:
            win.blit(layer,(self.x,self.y))
        
        self.animation_count +=1
        self.set_image()
    
    def move(self,keys):
        prev_action, prev_direction = self.action, self.direction
        
        # self.handle_attack()
        # if self.action_type == "attack":
        #     return
        
        if keys[pygame.K_LEFT]:
            self.direction = "left"
            if self.action not in["jump","falling"]:
                self.action = "walk"
            
            self.x -= self.vel
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            if self.action not in["jump","falling"]:
                self.action = "walk"
            
            self.x += self.vel
        elif self.action_type != "attack" and not self.action in ["jump", "falling"]:
            self.action = "stand"    
            
            
        self.handle_jump(keys)
        if self.jumping:
            return
            
        if self.action != prev_action or self.direction != prev_direction:
            self.animation_count = 0
        
    def handle_jump(self,keys):
        if self.jumping:
            self.jump_count += 1
            self.y -= self.JUMP_VEL
            if self.jump_count > self.jump_duration:
                self.jumping = False
                self.jump_count = 0
        if keys[pygame.K_x]:
            self.action = "jump"
            self.jumping = True
            self.jump_count = 1   
    
    # def handle_attack(self):
    #     pressed = pygame.key.get_pressed()
        
    #     if any(pressed):
    #         self.action_type ="attack"
    #         self.action = "chop"