import pygame
from button import Button
from character import player
from enemy import Enemy
from projectile import *
from load_image import *
from load_music import *
from data_map import *
from load_map import Map

WIDTH, HEIGHT = 1080, 720

#Khởi tạo
pygame.init()
pygame.font.init()


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
font =  pygame.font.Font(os.path.join('asset','Font',"dejavusans-boldoblique.ttf"), 20)
selected_button = 0
# Biến kiểm soát phần menu
main_menu = True
game_over = False
button_new = Button(860, 290, 200, 50, "Chơi mới")
button_continue = Button(860, 357, 200, 50, "Tiếp tục")
button_load = Button(860, 424, 200, 50, "Tải")
button_setting = Button(860, 491, 200, 50, "Cài đặt")
button_exit = Button(860, 558, 200, 50, "Thoát game")
buttons = [button_new, button_continue, button_load, button_setting, button_exit]




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
    global selected_button, run

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                channel_select_bar.play(select_bar_sound)
                if selected_button == 0:
                    selected_button = len(buttons) - 1
                else:
                    selected_button -= 1
            elif event.key == pygame.K_DOWN:
                channel_select_bar.play(select_bar_sound)
                if selected_button == len(buttons) -1:
                    selected_button = 0
                else:
                    selected_button += 1
            elif event.key == pygame.K_RETURN:
                channel_select_bar.play(accept_sound)
                if selected_button == 0:
                    start_game()
                elif selected_button == 1:
                    print('Tiếp tục')
                elif selected_button == 2:
                    print('Tải')
                elif selected_button == 3:
                    print('Cài đặt')
                elif selected_button == 4:
                    run = False


#Xử lý các đòn đánh
def playerattack(enemies):
    for enemy in enemies:
        if man.melee.hitbox[1] - man.melee.hitbox[3] < enemy.hitbox[1] + enemy.hitbox[3] and man.melee.hitbox[1] + man.melee.hitbox[3] > enemy.hitbox[1]:
            if man.isAttack and man.prev_action == "right":
                if (man.melee.hitbox[0] + man.melee.hitbox[2]) > enemy.hitbox[0] and man.melee.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                    enemy.hit() 
            elif man.isAttack and man.prev_action == "left":
                if (man.melee.hitbox[0] - man.melee.hitbox[2]) < enemy.hitbox[0]  and man.melee.hitbox[0] > enemy.hitbox[0] :
                    enemy.hit() 
            else:
                enemy.ishitted = False
#Xử lý khi bị tấn công
def playerhitted(enemies, man, WIN):
    for enemy in enemies:
        if enemy.visible == True:
            if man.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and man.hitbox[1] + man.hitbox[3] > enemy.hitbox[1]:
                if (man.hitbox[0] + man.hitbox[2]) > enemy.hitbox[0] and man.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                        man.hit(WIN) 
                    
#Thông tin các Màn 
map_0 = "asset/Map/Map_tutorial.tmx"
map_1 = "asset/Map/Map_1.tmx"
map_2 = "asset/Map/Map_2.tmx"
map_3 = "asset/Map/Map_3.tmx"
map_4 = "asset/Map/Map_4.tmx"
lstmap= [map_0,map_1,map_2,map_3,map_4]
index_map = 0
enemies = []
man = player(0,0,0,0)


# Vẽ các màn chơi
def draw_map(map_filename):
    global enemies, man
    game_map = Map(map_filename)
    map_now = game_map
    map_surface = game_map.make_map(bg[index_map])
    enemies = draw_enemy(map_now, WIN)
    man = draw_player(map_now, WIN)
    return map_now, map_surface

map_inf = draw_map(lstmap[index_map])

#vẽ game
def draw_game(keys):  
    global main_menu, game_over,index_map, map_inf
    WIN.blit(map_inf[1], (0,0))
    man.draw(WIN)
    for enemy in enemies:
        enemy.draw(WIN, map_inf[0])
        
    if keys[pygame.K_ESCAPE]:
        main_menu = True
        game_over = False
        draw_map(lstmap[index_map])
        draw_menu()
    if man.health <= 0:
        WIN.blit(game_over_img, (0,0))
        text = "Nhấn ESC để về màn hình chính"
        text_render  = font.render(text, True, WHITE)
        WIN.blit(text_render, (350, 500))
        game_over = True
    if man.progress =="clear":
        index_map += 1
        man.progress = 0
        map_inf = draw_map(lstmap[index_map])
    pygame.display.update()
 
#Khởi tạo trò chơi
def start_game():
    global main_menu
    main_menu = False
    
    
# Vòng lặp game
run = True   
clock = pygame.time.Clock()
while run == True:
        main_sound(main_menu, game_over)
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
            draw_game(keys)
            man.move(keys, map_inf[0])
            playerattack(enemies)
            playerhitted(enemies, man,WIN)
            
pygame.quit() 

