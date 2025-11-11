import pygame
import math
import random

from norm_dim import Player, Box

def main(screen):
    clock = pygame.time.Clock()

    running = True
    global player, box
    player.original_img = pygame.Surface((30, 30))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Player.move now handles pushing the box when it collides.
        player.move(box, keys)

        screen.fill((0, 0, 0))
        player.draw(screen)
        box.draw(screen)

        pygame.display.flip()
        clock.tick(60)