import pygame
from classes import Wall, Door, Img


def map1n():
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    img1 = Img(675, 425, 'Resources\\misc\\flag_txt.png')
    img2 = Img(175, 125, 'Resources\\misc\\box_txt.png')
    img3 = Img(475, 330, 'Resources\\misc\\button_txt.png')
    return walls, [img1, img2, img3]

def map1o():
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls, []

def map2n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 400, 300
        box.x, box.y, box.state = 200, 150, 2
        button.x, button.y = 600, 450
        end.x, end.y, end.active, end.initialized = 750, 550, False, True

    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    wall5 = Wall(480, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4, wall5]
    img1 = Img(675, 425, 'Resources\\misc\\space_up.png')
    return walls, [img1]

def map2o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 400, 300
        box.x, box.y, box.state = 200, 150, 2
        button.x, button.y = 600, 450
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls, []

def map3n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 200, 150, 2
        button.x, button.y, button.state = 400, 290, 2
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    wall1 = Wall(0, 50, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 50, 20, 500)  # Vertical wall
    wall4 = Wall(780, 50, 20, 500)  # Vertical wall
    walls = [wall1, wall2, wall4]
    door1 = Door(0, 530, 800, 20)
    doors = [door1]
    return walls, doors, []

def map3o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 200, 150, 2
        button.x, button.y, button.state = 400, 290, 2
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 50, 20, 550)  # Vertical wall
    wall3 = Wall(0, 530, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 50, 20, 550)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls, []


def map4n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active, end.initialized = 775, 585, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 540)  # Vertical wall
    wall3 = Wall(0, 520, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 540)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls, []

def map4o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active, end.initialized = 775, 585, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 550)  # Vertical wall
    wall3 = Wall(0, 490, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 550)  # Vertical wall
    wall5 = Wall(0, 550, 800, 20)  # Horizontal wall
    walls = [wall1, wall2, wall3, wall4, wall5]
    return walls, []

def map5n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 350, 2
        button.x, button.y, button.state = 290, 290, 2
        end.x, end.y, end.active, end.initialized = 100, 50, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall

    wall5 = Wall(0, 100, 360, 20)  # Horizontal wall
    wall6 = Wall(470, 100, 350, 20)

    wall7 = Wall(360, 80, 100, 120)

    walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]
    return walls, []

def map5o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 350, 2
        button.x, button.y, button.state = 290, 290, 2
        end.x, end.y, end.active, end.initialized = 100, 50, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 600)  # Vertical wall
    wall3 = Wall(0, 580, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 600)  # Vertical wall

    wall5 = Wall(0, 100, 360, 20)  # Horizontal wall
    wall6 = Wall(440, 100, 360, 20)

    wall7 = Wall(360, 80, 70, 120)

    walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]
    return walls, []

def map6n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active, end.initialized = 775, 575, False, True
    wall1 = Wall(0, 50, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 50, 20, 500)  # Vertical wall
    wall3 = Wall(0, 530, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 50, 20, 500)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls, []

def map6o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active, end.initialized = 775, 575, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 550)  # Vertical wall
    wall3 = Wall(0, 530, 780, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 580)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls, []

def map7n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 400, 500, 1
        button.x, button.y, button.state = 400, 500, 0
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    door = Door(0, 400, 800, 20)
    walls = []
    doors = [door]
    img1 = Img(425, 525, 'Resources\\misc\\mouse_no.png')
    return walls, doors, [img1]

def map7o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 400, 500, 1
        button.x, button.y, button.state = 400, 500, 0
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    door = Door(0, 400, 800, 20)
    walls = []
    doors = [door]
    return walls, doors, []

def map8n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active, end.initialized = 775, 575, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 550)  # Vertical wall
    wall3 = Wall(0, 530, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 550)  # Vertical wall
    walls = [wall1, wall2, wall3, wall4]
    return walls, []

def map8o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 2
        button.x, button.y, button.state = 300, 300, 2
        end.x, end.y, end.active, end.initialized = 775, 575, False, True
    wall1 = Wall(0, 0, 800, 20)  # Horizontal wall
    wall2 = Wall(0, 0, 20, 520)  # Vertical wall
    wall3 = Wall(0, 500, 800, 20)  # Horizontal wall
    wall4 = Wall(780, 0, 20, 520)  # Vertical wall
    wall5 = Wall(0, 550, 800, 20)  # Horizontal wall
    walls = [wall1, wall2, wall3, wall4, wall5]
    return walls, []

def map9n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 0
        button.x, button.y, button.state = 300, 300, 0
        end.x, end.y, end.active, end.initialized = 775, 575, False, True
    wall1 = Wall(750, 550, 40, 40)
    walls = [wall1]
    return walls, []

def map9o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 100, 150, 0
        button.x, button.y, button.state = 300, 300, 0
        end.x, end.y, end.active, end.initialized = 775, 575, False, True
    wall1 = Wall(750, 550, 40, 40)
    walls = [wall1]
    return walls, []

def map10n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 400, 300, 1
        button.x, button.y, button.state = 500, 300, 0
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    wall1 = Wall(0, 400, 800, 5)  # Horizontal wall
    wall2 = Wall(790, 0, 10, 600)  # Vertical wall
    walls = [wall1, wall2]
    return walls, []

def map10o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 400, 300, 1
        button.x, button.y, button.state = 500, 300, 0
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    wall1 = Wall(0, 405, 800, 5)  # Horizontal wall
    wall2 = Wall(790, 0, 10, 600)  # Vertical wall
    walls = [wall1, wall2]
    return walls, []

def map11n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 400, 500, 1
        button.x, button.y, button.state = 500, 500, 0
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    wall1 = Wall(0, 295, 800, 20)  # Horizontal wall
    walls = [wall1]
    return walls, []

def map11o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 100, 100
        box.x, box.y, box.state = 400, 500, 1
        button.x, button.y, button.state = 500, 500, 0
        end.x, end.y, end.active, end.initialized = 750, 550, False, True
    door1 = Door(0, 300, 800, 20)
    walls = []
    doors = [door1]
    return walls, doors, []

def map12n(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 700, 300, 0
        button.x, button.y, button.state = 400, 500, 1
        end.x, end.y, end.active, end.initialized = 50, 50, True, True
    wall2 = Wall(600, 100, 20, 490)
    wall3 = Wall(100, 0, 20, 70)
    wall4 = Wall(0, 125, 100, 20)
    wall5 = Wall(90, 90, 10, 30)
    walls = [wall2, wall3, wall4, wall5]
    door1 = Door(100, 75, 520, 20)
    doors = [door1]
    return walls, doors, []

def map12o(player, box, button, end):
    if not end.initialized:
        player.x, player.y = 200, 200
        box.x, box.y, box.state = 700, 300, 0
        button.x, button.y, button.state = 400, 500, 1
        end.x, end.y, end.active, end.initialized = 50, 50, True, True
    wall1 = Wall(0, 75, 610, 20)
    wall2 = Wall(600, 75, 20, 510)
    wall3 = Wall(100, 0, 20, 70)
    wall4 = Wall(0, 125, 100, 20)
    wall5 = Wall(90, 90, 10, 30)
    walls = [wall1, wall2, wall3, wall4, wall5]
    return walls, []
