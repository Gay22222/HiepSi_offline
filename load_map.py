import pygame
import pytmx
from load_image import *
from enemy import Enemy


#Tạo đối tượng Map
class Map:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.enemies = []
    
    def make_enemy(self):
        objectgroup = None
        for layer in self.tmxdata.layers:
            if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == "enemy1":
                objectgroup = layer
                break

        if objectgroup:
            for obj in objectgroup:
                x = obj.x
                y = obj.y- 13
                width = obj.width
                height = obj.height
                end =  self.tmxdata.tilewidth
                enemy = Enemy(x, y, width, height, end)  
                self.enemies.append(enemy) 
      
      
      
        
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
        # self.make_enemy()
        # for enemy in self.enemies:
        #     enemy.update()
        #     enemy.draw(background_surface)

        return background_surface




