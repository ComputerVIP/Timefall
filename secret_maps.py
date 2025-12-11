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

def map2n(player, enemy, end):
    if not end.initialized:
        player.x, player.y = 300, 300
        enemy.x, enemy.y = 500, 300
        end.x, end.y, end.active, end.initialized = 650, 450, True, True
    return []

def map2o(player, enemy, end):
    if not end.initialized:
        player.x, player.y = 300, 300
        enemy.x, enemy.y = 500, 300
        end.x, end.y, end.active, end.initialized = 650, 450, True, True
    return []

def map3n(player, enemy, end):
    if not end.initialized:
        player.x, player.y = 300, 300
        enemy.x, enemy.y = 500, 300
        end.x, end.y, end.active, end.initialized = 650, 450, True, True

    wall1 = Wall(400, 0, 20, 800)  # Horizontal wall
    walls = [wall1]
    return walls

def map3o(player, enemy, end):
    if not end.initialized:
        player.x, player.y = 300, 300
        enemy.x, enemy.y = 500, 300
        end.x, end.y, end.active, end.initialized = 650, 450, True, True
    return []