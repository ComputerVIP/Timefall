import pygame
from classes import Player, Box, Button, End
from maps import *
from utils import wrap_map

def main(screen, player=None, box=None, button=None, end=None):
    
    # create objects if not provided
    if player is None:
        player = Player(400, 300, 2)
    if box is None:
        box = Box(200, 150, 1)
    if button is None:
        button = Button(500, 350, 1)
    if end is None:
        end = End(750, 550, 1, active=False, level = 1)
    
    map_functions = {
        1: wrap_map(map1o, needs_args=False),
        2: wrap_map(map2o, needs_args=True),
        3: wrap_map(map3o, needs_args=True),
        4: wrap_map(map4o, needs_args=True),
        5: wrap_map(map5o, needs_args=True),
        6: wrap_map(map6o, needs_args=True),
        7: wrap_map(map7o, needs_args=True),
        8: wrap_map(map8o, needs_args=True),
    }
    walls, doors, imgs = map_functions[end.level](player, box, button, end)

    try:
        doors
    except NameError:
        doors = []

    # ensure only the player's state switches to this mode
    #player.state = 1

    clock = pygame.time.Clock()
    running = True

    # removed overwriting player.original_img

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                # use event.key so the switch isn't missed
                if event.key == pygame.K_SPACE:
                    return screen, player, box, button, end, 'norm'
                if event.key == pygame.K_ESCAPE:
                    return screen, player, box, button, end, 'pause'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if button.get_rect().collidepoint(event.pos):
                        if button.state == 0:
                            button.state = 1
                        elif button.state == 1:
                            button.state = 0
                        else:
                            button.state = 2
                    if box.get_rect().collidepoint(event.pos):
                        if box.state == 1:
                            box.state = 0
                        elif box.state == 0:
                            box.state = 1
                        else:
                            box.state = 2

        keys = pygame.key.get_pressed()
        try:
            player.move(box, keys, walls, doors)
        except:
            return screen, player, box, button, end, 'menu'
        screen.fill((44, 4, 28))

        if player.state in (1, 2):
            player.draw(screen, (215, 38, 56))
        if box.state in (1, 2):
            box.draw(screen, (62, 74, 102))
        if end.state in (1, 2):
            if end.active == True:
                end.img.fill((0, 200, 0))
            else:
                end.img.fill((100, 255, 100))
            end.draw(screen)
        if button.state in (1, 2):
            button.draw(screen, (106, 143, 63))
        for i in walls:
            i.draw(screen, (227, 178, 60))
        for i in doors:
            if i.active == True:
                i.draw(screen, (150, 75, 0))
            else:
                i.draw(screen, None)
        for i in imgs:
            i.draw(screen)

        level = end.level
        
        button.activate(box, end, doors)
        end.next_level(player)

        if end.level == (level + 1):
            player.x = 400
            player.y = 300
            return screen, player, box, button, end, 'opp'
            
        
        pygame.display.flip()
        clock.tick(60)
