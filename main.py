from norm_dim import main as norm_main
from opp_dim import main as opp_main
import pygame

def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((800, 600)) 
    pygame.display.set_caption("Dimensional Simulation Selector")

    font = pygame.font.Font(None, 36)
    norm_text = font.render("Press Space to play", True, (255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    norm_main(screen)

        screen.fill((0, 0, 0))
        screen.blit(norm_text, (200, 250))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()