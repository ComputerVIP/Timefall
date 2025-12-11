import pygame
from secret_classes import Wall, Flip


def map1n():
    return []

def map1o():
    return []

def map2n(player, enemy, end):
    if not end.initialized:
        player.x, player.y = 300, 300
        enemy.x, enemy.y = 500, 300
        end.x, end.y, end.active, end.initialized = 650, 450, True, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map2o(player, enemy, end):
    if not end.initialized:
        player.x, player.y = 300, 300
        enemy.x, enemy.y = 500, 300
        end.x, end.y, end.active, end.initialized = 650, 450, True, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls

def map3n(player, enemy, end):
    if not end.initialized:
        player.x, player.y = 300, 300
        enemy.x, enemy.y = 500, 300
        end.x, end.y, end.active, end.initialized = 650, 450, True, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    wall5 = Wall(400, 300, 20, 400)  # Vertical wall
    wall6 = Wall(420, 300, 50, 50)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4, wall5, wall6]
    flip1 = Flip(400, 0, 400, 600)
    flips = [flip1]
    return walls, flips

def map3o(player, enemy, end):
    if not end.initialized:
        player.x, player.y = 300, 300
        enemy.x, enemy.y = 500, 300
        end.x, end.y, end.active, end.initialized = 650, 450, True, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    flip1 = Flip(400, 0, 400, 600)
    flips = [flip1]
    return walls, flips