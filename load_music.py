import pygame
import os


pygame.mixer.init()

#tạo các kênh âm thanh
channel_menu = pygame.mixer.Channel(0)
channel_game = pygame.mixer.Channel(1)
channel_move = pygame.mixer.Channel(2)
channel_game_over = pygame.mixer.Channel(3)
channel_select_bar = pygame.mixer.Channel(4)


# Hàm tải âm thanh từ asset
def load_sound(type, name):
    sound_file = os.path.join('asset', type, name)
    sound = pygame.mixer.Sound(sound_file)
    return sound




#Tải âm thanh
main_menu_music = load_sound('Music' ,'bgmED01.ogg')
game_music = load_sound('Music' ,"bgmED02.ogg")
select_bar_sound = load_sound('Music' ,"Cursor2.ogg")
accept_sound = load_sound('Music' ,"Decision1.ogg")
jump_sound = load_sound('Music' ,"Jump1.ogg")
dash_sound = load_sound('Music' ,"Evasion1.ogg")
attack_sound = load_sound('Music' ,"Attack3.ogg")
hitted_sound = load_sound('Music' ,"Damage1.ogg")
game_over_sound = load_sound('Music' ,"Gameover2.ogg")


#Phát âm thanh
def main_sound(main_menu, game_over):
    if game_over:
        channel_game.stop()
        channel_menu.stop()
        channel_move.stop()
        if channel_game_over.get_busy():
            return
        else:
            channel_game_over.play(game_over_sound)
    if not game_over:
        channel_game_over.stop()
    if main_menu:
        channel_game.stop()

        if channel_menu.get_busy():
            return
        else:
            channel_menu.play(main_menu_music)
    elif not main_menu:
        channel_menu.stop()
        if channel_game.get_busy():
            return
        else:
            channel_game.play(game_music)
    
    
