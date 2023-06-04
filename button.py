import pygame
import os
pygame.font.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW  = (255, 160, 0)


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(os.path.join('asset','Font',"dejavusans-boldoblique.ttf"), 30)
        self.text_surf = self.font.render(text, True, BLACK)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw_yellow(self, surface):
        self.text_surf = self.font.render(self.text, True, YELLOW)
        surface.blit(self.text_surf, self.text_rect)
        
    def draw_black(self,surface):
        self.text_surf = self.font.render(self.text, True, BLACK)
        surface.blit(self.text_surf, self.text_rect)
