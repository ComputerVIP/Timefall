import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Timefall")

    font = pygame.font.Font(None, 36)
    norm_text = font.render("Press Space to play", True, (255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Enter the game loop manager which will call norm/opp mains
                    from norm_dim import main as norm_main
                    # start the norm mode; it will create objects if None
                    result = norm_main(screen, None, None, None, None)
                    if not result:
                        running = False
                        break
                    screen, player, box, button, end, next_state = result

                    state = next_state
                    # loop between modes until quit
                    while True:
                        if state == 'opp':
                            from opp_dim import main as opp_main
                            result = opp_main(screen, player, box, button, end)
                        else:
                            from norm_dim import main as norm_main
                            result = norm_main(screen, player, box, button, end)

                        if not result:
                            running = False
                            break

                        screen, player, box, button, end, state = result
        screen.fill((0, 0, 0))
        screen.blit(norm_text, (200, 250))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()