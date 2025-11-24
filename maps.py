import pygame
from classes import Wall, Door


def map1n():
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map1o():
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map2n(player, box, button, end):
    if button.x != 600 and button.y != 450:
        player.x, player.y = 400, 300
        box.x, box.y, box.state = 200, 150, 2
        button.x, button.y = 600, 450
        end.x, end.y, end.active = 750, 550, False

    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    wall5 = Wall(480, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4, wall5]
    return walls

def map2o(player, box, button, end):
    if button.x != 600 and button.y != 450:
        player.x, player.y = 400, 300
        box.x, box.y, box.state = 200, 150, 2
        button.x, button.y = 600, 450
        end.x, end.y, end.active = 750, 550, False
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map3n(player, box, button, end):
    if button.x != 400 and button.y != 300:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 200, 150, 2
        button.x, button.y, button.state = 400, 290, 2
        end.x, end.y, end.active = 750, 550, False
    wall1 = Wall(0, 50, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 50, 20, 500)  # Vertical wall
    wall4 = Wall(780, 50, 20, 500)  # Vertical wall
    walls = [wall1, wall2, wall4]
    door1 = Door(0, 530, 800, 20)
    doors = [door1]
    return walls, doors

def map3o(player, box, button, end):
    if button.x != 400 and button.y != 300:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 200, 150, 2
        button.x, button.y, button.state = 400, 290, 2
        end.x, end.y, end.active = 750, 550, False
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 50, 20, 550)  # Vertical wall
    wall3 = Wall(0, 530, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 50, 20, 550)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map4n(player, box, button, end):
    if button.x != 300 and button.y != 300:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active = 775, 575, False
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 550)  # Vertical wall
    wall3 = Wall(0, 530, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 550)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map4o(player, box, button, end):
    if button.x != 300 and button.y != 300:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active = 775, 575, False
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 520)  # Vertical wall
    wall3 = Wall(0, 500, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 520)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map5n(player, box, button, end):
    if button.x != 300 and button.y != 300:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active = 775, 575, False
    wall1 = Wall(0, 50, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 50, 20, 500)  # Vertical wall
    wall3 = Wall(0, 530, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 50, 20, 500)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map5o(player, box, button, end):
    if button.x != 300 and button.y != 300:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active = 775, 575, False
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 550)  # Vertical wall
    wall3 = Wall(0, 530, 780, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 580)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls