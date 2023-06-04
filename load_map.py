import pygame
import pytmx
from load_image import *

class Map:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    if gid != 0:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self):
        background_surface = pygame.Surface((self.width, self.height))
        background_image = bg 
        background_surface.blit(bg, (0, 0))
        self.render(background_surface)
        return background_surface



