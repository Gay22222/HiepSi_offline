import pygame
import os


pygame.mixer.init()
channel_menu = pygame.mixer.Channel(0)
channel_game = pygame.mixer.Channel(1)
channel_move = pygame.mixer.Channel(2)

def load_sound(type, name):
    sound_file = os.path.join('asset', type, name)
    sound = pygame.mixer.Sound(sound_file)
    return sound






main_menu_music = load_sound('Music' ,'bgmED01.ogg')
game_music = load_sound('Music' ,"bgmED02.ogg")
select_bar_sound = load_sound('Music' ,"Cursor2.ogg")
accept_sound = load_sound('Music' ,"Decision1.ogg")
jump_sound = load_sound('Music' ,"Jump1.ogg")
dash_sound = load_sound('Music' ,"Evasion1.ogg")
attack_sound = load_sound('Music' ,"Attack3.ogg")