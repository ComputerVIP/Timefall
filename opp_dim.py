import pygame
import math
import random

from norm_dim import Player, Box

def main(screen):
    clock = pygame.time.Clock()

    running = True
    player = Player(400, 300, None)
    box = Box(200, 150)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if box.get_rect().colliderect(player.get_rect()):
                box.move(player.speed)

        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill((0, 0, 0))
        player.draw(screen, player.x, player.y)
        box.draw(screen, box.x, box.y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()