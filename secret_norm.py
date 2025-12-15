import pygame
from secret_classes import Player, Enemy, End
from secret_maps import *

def sec_main_norm(screen, player=None, enemy=None, end=None):
    from main import main as norm_main
    print("Starting secret norm mode")

    # create objects if not provided
    if player is None:
        player = Player(300, 300, 2)
    if enemy is None:
        enemy = Enemy(500, 300, 2)
    if end is None:
        end = End(650, 450, 2, active=True, level=1) #Change level to help test, otherwise leave at 1

    if end.level == 1:
        walls = map1n()
    elif end.level == 2:
        walls = map2n(player, enemy, end)
    elif end.level == 3:
        walls, flips = map3n(player, enemy, end)

    clock = pygame.time.Clock()
    last_update = 0
    frame_delay = 33
    running = True
    can_do = 0

    while running:
        now = pygame.time.get_ticks()
        if now - last_update >= frame_delay:
            can_do += 1
            last_update = now
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                # use event.key so the switch isn't missed
                if event.key == pygame.K_SPACE:
                    return screen, player, enemy, end, 'opp'
                if event.key == pygame.K_ESCAPE:
                    return screen, player, enemy, end, 'pause'
                if event.key == pygame.K_r:
                    end.initialized = False
                    if end.level == 1:
                        walls = map1n()
                    elif end.level == 2:
                        walls = map2n(player, enemy, end)
                    elif end.level == 3:
                        walls, flips = map3n(player, enemy, end)
        screen.fill((234, 248, 240))
        try:
            for f in flips:
                f.draw(screen, 'norm')
                f.activate(player, enemy)
        except Exception as e:
            pass

        keys = pygame.key.get_pressed()
        try:
            player.move(keys, walls, enemy, 'norm')
            enemy.move(keys, walls, player, 'norm')
        except Exception as e:
            return 

        if player.state in (0, 2):
            player.draw(screen)

        if enemy.state in (0, 2):
            enemy.draw(screen)

        if can_do > 1:
            end.draw(screen, True)
            can_do = 0
        else:
            end.draw(screen, False)
        try:
            for i in walls:
                i.draw(screen, (60, 142, 227))
        except Exception as e:
            pass

        level = end.level



        end.next_level(player)

        if end.level == level + 1:
            player.x, player.y = 300, 300
            enemy.x, enemy.y = 500, 300
            return screen, player, enemy, end, 'norm'


        pygame.display.flip()
        clock.tick(60)
