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
        end = End(650, 450, 2, active=False, level=1) #Change level to help test, otherwise leave at 1

    if end.level == 1:
        walls,imgs = map1n()
    elif end.level == 2:
        walls,imgs = map2n(player, box, button, end)
    elif end.level == 3:
        walls, doors, imgs = map3n(player, box, button, end)
    elif end.level == 4:
        walls,imgs = map4n(player, box, button, end)
    elif end.level == 5:
        walls,imgs = map5n(player, box, button, end)
    elif end.level == 6:
        walls,imgs = map6n(player, box, button, end)
    elif end.level == 7:
        walls,doors, imgs = map7n(player, box, button, end)
    elif end.level == 8:
        walls,imgs = map8n(player, box, button, end)
    elif end.level == 9:
        walls, imgs = map9n(player, box, button, end)
    elif end.level == 10:
        walls, imgs = map10n(player, box, button, end)
    elif end.level == 11:
        walls, imgs = map11n(player, box, button, end)
    elif end.level == 12:
        walls, doors, imgs = map12n(player, box, button, end)

    try:
        doors
    except NameError:
        doors = []

    clock = pygame.time.Clock()
    last_update = 0
    frame_delay = 33
    running = True
    can_do = 0
    can_do2 = 0

    while running:
        now = pygame.time.get_ticks()
        if now - last_update >= frame_delay:
            can_do += 1
            can_do2 += 1
            last_update = now
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                # use event.key so the switch isn't missed
                if event.key == pygame.K_SPACE:
                    return screen, player, box, button, end, 'opp'
                if event.key == pygame.K_ESCAPE:
                    return screen, player, box, button, end, 'pause'
                if event.key == pygame.K_r:
                    end.initialized = False
                    if end.level == 1:
                        walls,imgs = map1n()
                    elif end.level == 2:
                        walls,imgs = map2n(player, box, button, end)
                    elif end.level == 3:
                        walls, doors, imgs = map3n(player, box, button, end)
                    elif end.level == 4:
                        walls,imgs = map4n(player, box, button, end)
                    elif end.level == 5:
                        walls,imgs = map5n(player, box, button, end)
                    elif end.level == 6:
                        walls,imgs = map6n(player, box, button, end)
                    elif end.level == 7:
                        walls,doors, imgs = map7n(player, box, button, end)
                    elif end.level == 8:
                        walls,imgs = map8n(player, box, button, end)
                    elif end.level == 9:
                        walls, imgs = map9n(player, box, button, end)
                    elif end.level == 10:
                        walls, imgs = map10n(player, box, button, end)
                    elif end.level == 11:
                        walls, imgs = map11n(player, box, button, end)
                    elif end.level == 12:
                        walls, doors, imgs = map12n(player, box, button, end)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if button.get_rect().collidepoint(event.pos) and box.get_rect().collidepoint(event.pos):
                        # prioritize button if both clicked
                        if button.state == 0:
                            button.state = 1
                        elif button.state == 1:
                            button.state = 0
                        else:
                            button.state = 2
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
        if box.state == 0:
            if end.level == 9 or end.level ==10 or end.level == 12:
                box.pushable = False
        elif end.level == 9 or end.level == 10 or end.level ==11 or end.level == 12 and box.state != 0:
            box.pushable = True

        try:
            player.move(box, keys, walls, doors, 'norm')
        except Exception as e:
            return screen, player, box, button, end, 'menu'
        screen.fill((234, 248, 240))
        

        if player.state in (0, 2):
            player.draw(screen)

        if button.state in (0, 2):
            button.draw(screen, 'norm')

        if box.state in (0, 2):
            box.draw(screen, 'norm')
        
        if can_do > 1:
            end.draw(screen, True)
            can_do = 0
        else:
            end.draw(screen, False)

        for i in walls:
            i.draw(screen, (60, 142, 227))

        for i in doors:
            if i.active == True:
                i.draw(screen, (150, 75, 0))
            else:
                i.draw(screen, None)
        if imgs:
            if can_do2 > 3:
                for i in imgs:
                    if i.x == 675 or i.x == 425:
                        if i.img_path == 'Resources\\misc\\space_up.png':
                            i.img_path = 'Resources\\misc\\space_down.png'
                            i.img = pygame.image.load(i.img_path)
                        elif i.img_path == 'Resources\\misc\\space_down.png':
                            i.img_path = 'Resources\\misc\\space_up.png'
                            i.img = pygame.image.load(i.img_path)
                        if i.img_path == 'Resources\\misc\\mouse_no.png':
                            i.img_path = 'Resources\\misc\\mouse_yes.png'
                            i.img = pygame.image.load(i.img_path)
                        else:
                            if i.img_path == 'Resources\\misc\\mouse_yes.png':
                                i.img_path = 'Resources\\misc\\mouse_no.png'
                                i.img = pygame.image.load(i.img_path)
                    i.draw(screen)
                can_do2 = 0
            else:
                for i in imgs:
                    i.draw(screen)

        level = end.level
        
        button.activate(box, end, doors)
        end.next_level(player)

        if end.level == (level + 1):
            player.x = 400
            player.y = 300
            button.active = False
            return screen, player, box, button, end, 'norm'

        pygame.display.flip()
        clock.tick(60)
