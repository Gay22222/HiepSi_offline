import pygame
from button import Button
from object import player
from object import enemy
from projectile import *
from load_image import *
from load_music import *
from load_map import Map

WIDTH, HEIGHT = 1080, 720


pygame.init()
pygame.font.init()
pygame.mixer.init()
# Thông tin game
TITLE = "Hiệp sĩ Offline"
MAX_FPS = 27
# Màu
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW  = (255, 160, 0)


# Cửa sổ game
WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)



selected_button = 0
# Biến kiểm soát phần menu
main_menu = True
button_new = Button(860, 290, 200, 50, "Chơi mới")
button_continue = Button(860, 357, 200, 50, "Tiếp tục")
button_load = Button(860, 424, 200, 50, "Tải")
button_setting = Button(860, 491, 200, 50, "Cài đặt")
button_exit = Button(860, 558, 200, 50, "Thoát game")
buttons = [button_new, button_continue, button_load, button_setting, button_exit]

# Khởi tạo đối tượng
man = player(100, 600, 64, 64)
melee = AttackMelee(man.x,man.y)
slime = enemy(500 , 600 , 64, 64, 1000)

#Âm thanh nền
def main_sound():
    if main_menu:
        if channel_menu.get_busy():
            return
        else:
            channel_menu.play(main_menu_music)
    else:
        channel_menu.stop()
        if channel_game.get_busy():
            return
        else:
            channel_game.play(game_music)
#Vẽ menu
def draw_menu():
    WIN.blit(main_menu_img, (0, 0))
    WIN.blit(select_bar, (820,90))
    for i, button in enumerate (buttons):
        if i == selected_button:
            button.draw_yellow(WIN)
        else:
            button.draw_black(WIN)
    pygame.display.update()
#Tương tác với menu
def select_menu(event):
    global selected_button

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                select_bar_sound.play()
                if selected_button == 0:
                    selected_button = len(buttons) - 1
                else:
                    selected_button -= 1
            elif event.key == pygame.K_DOWN:
                select_bar_sound.play()
                if selected_button == len(buttons) -1:
                    selected_button = 0
                else:
                    selected_button += 1
            elif event.key == pygame.K_RETURN:
                accept_sound.play()
                if selected_button == 0:
                    start_game()
                elif selected_button == 1:
                    print('Tiếp tục')
                elif selected_button == 2:
                    print('Tải')
                elif selected_button == 3:
                    print('Cài đặt')
                elif selected_button == 4:
                    pygame.quit()


def playerattack():
    if man.isAttack and man.prev_action == "right":
        if (man.melee.hitbox[0] + man.melee.hitbox[2]) > slime.hitbox[0] and man.melee.hitbox[0] < slime.hitbox[0] + slime.hitbox[2]:
            slime.hit() 
    elif man.isAttack and man.prev_action == "left":
        if (man.melee.hitbox[0] - man.melee.hitbox[2]) < slime.hitbox[0]  and man.melee.hitbox[0] > slime.hitbox[0] :
            slime.hit() 
    else:
        slime.ishitted = False

map_filename = "asset/Map/Map_tutorial.tmx"
game_map = Map(map_filename)

# Vẽ bản đồ
map_surface = game_map.make_map()

#vẽ game
def draw_game():  

    WIN.blit(map_surface, (0,0))
    man.draw(WIN)
    slime.draw(WIN)
    pygame.display.update()
 

 
def start_game():
    global main_menu
    main_menu = False
    draw_game()


def main():
    clock = pygame.time.Clock()
    run = True    
    while run:
        main_sound()
        keys = pygame.key.get_pressed()
        clock.tick(MAX_FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if main_menu:
                draw_menu()   
                select_menu(event)
        if not main_menu:        
            man.move(keys)
            draw_game()
            playerattack()
    pygame.quit() 

if __name__ == "__main__":
    main()

