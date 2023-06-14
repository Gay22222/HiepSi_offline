import pygame
import pytmx
from load_image import *
from enemy import Enemy


#Tạo đối tượng Map
class Map:
    #Khởi tạo
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        
      
    #Lấy thông tin layer từ file tmx
    def get_level_data(self, layer_name):
        level_data = []
        layer = self.tmxdata.get_layer_by_name(layer_name)
        if layer:
            for y in range(self.tmxdata.height):
                row = []
                for x in range(self.tmxdata.width):
                    tile = layer.data[y][x]
                    row.append(tile if tile else 0)
                level_data.append(row)
        return level_data

    #Xử lý bản đồ
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    if gid != 0:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
    #Vẽ bản đò
    def make_map(self, bg):
        background_surface = pygame.Surface((self.width, self.height))
        background_image = bg 
        background_surface.blit(bg, (0, 0))
        self.render(background_surface)
        return background_surface




