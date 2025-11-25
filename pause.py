import pygame

def pause(screen):
    font = pygame.font.Font(None, 52)
    pause_text = font.render("Game Paused", True, (255, 255, 255))
    instruction_text = font.render("Press ESC to Resume, M for main menu", True, (255, 255, 255))

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'norm'
                if event.key == pygame.K_m:
                    return 'menu'

        screen.fill((0, 0, 0))
        screen.blit(pause_text, (250, 200))
        screen.blit(instruction_text, (150, 300))
        pygame.display.flip()

    return True