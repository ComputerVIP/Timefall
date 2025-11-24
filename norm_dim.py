import pygame
from classes import Player, Box, Button, End
from maps import *

def main(screen, player=None, box=None, button=None, end=None):
    # create objects if not provided
    if player is None:
        player = Player(400, 300, 2)
    if box is None:
        box = Box(200, 150, 0)
    if button is None:
        button = Button(500, 350, 0)
    if end is None:
        end = End(750, 550, 2, active=False, level=3) #Change level to help test, otherwise leave at 1

    if end.level == 1:
        walls = map1n()
    elif end.level == 2:
        walls = map2n(player, box, button, end)
    elif end.level == 3:
        walls, doors = map3n(player, box, button, end)
    elif end.level == 4:
        walls = map4n(player, box, button, end)
    elif end.level == 5:
        walls = map5n(player, box, button, end)

    try:
        doors
    except NameError:
        doors = []

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                # use event.key so the switch isn't missed
                if event.key == pygame.K_SPACE:
                    return screen, player, box, button, end, 'opp'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if button.get_rect().collidepoint(event.pos):
                        button.state = 1 if button.state == 0 else 0
                    if box.get_rect().collidepoint(event.pos):
                        box.state = 1 if box.state == 0 else 0

        keys = pygame.key.get_pressed()
        player.move(box, keys, walls, doors)
        screen.fill((234, 248, 240))
        

        if player.state in (0, 2):
            player.draw(screen, (38, 215, 197))
        if box.state in (0, 2):
            box.draw(screen, (102, 82, 62))
        if end.state in (0, 2):
            if end.active == True:
                end.img.fill((0, 200, 0))
            else:
                end.img.fill((100, 255, 100))
            end.draw(screen)
        if button.state in (0, 2):
            button.draw(screen, (143, 63, 122))
        for i in walls:
            i.draw(screen, (60, 142, 227))
        for i in doors:
            if i.active == True:
                i.draw(screen, (150, 75, 0))
            else:
                i.draw(screen, None)

        level = end.level
        
        button.activate(box, end, doors)
        end.next_level(player)

        if end.level == (level + 1):
            player.x = 400
            player.y = 300
            return screen, player, box, button, end, 'norm'

        pygame.display.flip()
        clock.tick(60)
