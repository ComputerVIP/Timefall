import pygame
from classes import Player, Box, Button, End

def main(screen, player=None, box=None, button=None, end=None):
    # create objects if not provided
    if player is None:
        player = Player(400, 300, 2)
    if box is None:
        box = Box(200, 150, 0)
    if button is None:
        button = Button(600, 450, 0)
    if end is None:
        end = End(750, 550, 2, active=False)
    from maps import map1n
    walls = map1n()

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
        player.move(box, keys, walls)
        screen.fill((234, 248, 240))
        

        if player.state in (0, 2):
            player.draw(screen, (38, 215, 197))
        if box.state in (0, 2):
            box.draw(screen)
        if end.state in (0, 2):
            end.draw(screen)
        if button.state in (0, 2):
            button.draw(screen)
        for i in walls:
            i.draw(screen, (60, 142, 227))
        
        button.activate(box, end)
        end.next_level(player)

        pygame.display.flip()
        clock.tick(60)
