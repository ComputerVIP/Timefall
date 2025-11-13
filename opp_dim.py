import pygame
import math
import random
from classes import Player, Box, Button, End

def main(screen, player=None, box=None, button=None, end=None):
    from maps import map1o
    walls = map1o()
    # create objects if not provided
    if player is None:
        player = Player(400, 300, 2)
    if box is None:
        box = Box(200, 150, 1)
    if button is None:
        button = Button(600, 450, 1)
    if end is None:
        end = End(750, 550, 1, active=False)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if button.get_rect().collidepoint(event.pos):
                        button.state = 0 if button.state == 1 else 1
                    if box.get_rect().collidepoint(event.pos):
                        box.state = 0 if box.state == 1 else 1

        keys = pygame.key.get_pressed()
        player.move(box, keys, walls)
        screen.fill((44, 4, 28))

        if player.state in (1, 2):
            player.draw(screen, (215, 38, 56))
        if box.state in (1, 2):
            box.draw(screen)
        if end.state in (1, 2):
            end.draw(screen)
        if button.state in (1, 2):
            button.draw(screen)
        for i in walls:
            i.draw(screen, (227, 178, 60))
        
        button.activate(box, end)
        end.next_level(player)
        
        pygame.display.flip()
        clock.tick(60)
