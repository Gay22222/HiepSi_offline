import pytmx
from enemy import *
from character import *

def draw_enemy(map, win):
    enemies = []
    objectgroup = None
    for layer in map.tmxdata.layers:
            if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == "enemy1":
                objectgroup = layer
                break

    if objectgroup:
            for obj in objectgroup:
                x = obj.x
                y = obj.y- 13
                width = obj.width
                height = obj.height
                end =  obj.x + 170
                enemy = Enemy(x, y, width, height, end)  
                enemies.append(enemy) 
    for enemy in enemies:
        enemy.draw(win,map)
    return enemies


def draw_player(map, win):
    objectgroup = None
    for layer in map.tmxdata.layers:
            if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == "Player":
                objectgroup = layer
                break

    if objectgroup:
            for obj in objectgroup:
                x = obj.x
                y = obj.y
                width = 64
                height = 64
                man = player(x, y, width, height)
    man.draw(win)
    return man


# def draw_boss(map,win):
#     objectgroup = None
#     for layer in map.tmxdata.layers:
#             if isinstance(layer, pytmx.TiledObjectGroup) and layer.name == "Boss1":
#                 objectgroup = layer
#                 break

#     if objectgroup:
#             for obj in objectgroup:
#                 x = obj.x
#                 y = obj.y- 13
#                 width = obj.width
#                 height = obj.height
#                 end =  obj.x + 170
#                 boss = Enemy(x, y, width, height, end)
#     boss.draw(win)
#     return boss