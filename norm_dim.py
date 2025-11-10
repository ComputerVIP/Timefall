import pygame
try:
    if Player is None or Box is None:
        from classes import Player, Box
    else:
        from opp_dim import Player, Box
except NameError:
    from classes import Player, Box

def main(screen):
    clock = pygame.time.Clock()

    running = True
    global player, box
    player = Player(400, 300, None)
    box = Box(200, 150)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if box.rect.colliderect(player.rect):
                keys = pygame.key.get_pressed()
                box.move(player, keys)

        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill((0, 0, 0))
        player.draw(screen, player.x, player.y)
        box.draw(screen, box.x, box.y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()