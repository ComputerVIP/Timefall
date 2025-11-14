import pygame
from classes import Wall


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