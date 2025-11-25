import pygame
from classes import Player, Box, Button, End
from maps import *

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
    
    if end.level == 1:
        walls = map1o()
    elif end.level == 2:
        walls = map2o(player, box, button, end)
    elif end.level == 3:
        walls= map3o(player, box, button, end)
    elif end.level == 4:
        walls = map4o(player, box, button, end)
    elif end.level == 5:
        walls = map5o(player, box, button, end)

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
                        button.state = 0 if button.state == 1 else 1
                    if box.get_rect().collidepoint(event.pos):
                        box.state = 0 if box.state == 1 else 1

        keys = pygame.key.get_pressed()
        player.move(box, keys, walls, doors)
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

        level = end.level
        
        button.activate(box, end, doors)
        end.next_level(player)

        if end.level == (level + 1):
            player.x = 400
            player.y = 300
            return screen, player, box, button, end, 'opp'
            
        
        pygame.display.flip()
        clock.tick(60)
