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

        keys = pygame.key.get_pressed()

        # Player.move now handles pushing the box when it collides.
        player.move(box, keys)

        screen.fill((0, 0, 0))
        player.draw(screen)
        box.draw(screen)

        pygame.display.flip()
        clock.tick(60)