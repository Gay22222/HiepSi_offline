import pygame
import os

WIDTH, HEIGHT = 1080, 720


#Các hàm để xử lý ảnh 
def load_image(type, name):
    image = pygame.image.load(os.path.join('asset', type ,name))
    return image
    
def transform(image, width, height):
    image = pygame.transform.scale(image,(width, height))
    return image

def flip(image, horizontal , vertical):
    image = pygame.transform.flip(image,horizontal,vertical)
    return image

 
# Load hình nền
main_menu_img = load_image('bg','WorldMap.png')
main_menu_img = transform(main_menu_img,WIDTH,HEIGHT)
select_bar = load_image('bg',"Selectbar.png")
bg = [load_image('bg','Tower1.png'), load_image('bg','Night.png'),load_image('bg','Castle.png'),load_image('bg','DemonCastle.png'),load_image('bg','Devil.png')]
bg = [transform(bg_index,WIDTH,HEIGHT) for bg_index in bg]
game_over_img = load_image('bg','GameOver.png')
game_over_img = transform(game_over_img,WIDTH,HEIGHT)

#Load chuyển động nhân vật
walkRight = [load_image('character','R1.png'), load_image('character','R2.png'), load_image('character','R3.png')]
walkLeft = [flip(image,True, False) for image in walkRight]
jumpleft = load_image('character','JumpL.png')
jumpright = flip(jumpleft,True,False)
jumpleft = transform(jumpleft,45,50)
jumpright = transform(jumpright,45,50)

attackR = [load_image('Animation','A1.png'),load_image('Animation','A2.png'),load_image('Animation','A3.png')]
attackR = [transform(image,100, 100) for image in attackR]
attackL = [flip(image,True,False) for image in attackR]


#Load chuyển động quái
walkLeftE1 = [load_image('enemy','slime_L1.png'), load_image('enemy','slime_L2.png'), load_image('enemy','slime_L3.png')]
walkLeftE1 = [transform(image,45, 50) for image in walkLeftE1]
walkRightE1 = [flip(image,True, False) for image in walkLeftE1]


