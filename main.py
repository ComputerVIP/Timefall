import pygame
from pause import pause
from classes import Click
from secret_norm import sec_main_norm
from secret_opp import sec_main_opp

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Timefall")

    font = pygame.font.Font(None, 36)
    norm_text = font.render("Play", True, (255, 255, 255))
    exit_txt = font.render("Exit", True, (255, 255, 255))   

    play = Click(200, 250, 400, 50)
    exit = Click(350, 350, 100, 50)

    cnt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cnt += 1
                    if cnt == 3:
                        result = sec_main_norm(screen, None, None, None)
                        if not result: 
                            running = False
                            break
                        screen, player, enemy, end, next_state = result

                        state = next_state
                        # loop between modes until quit
                        while True:
                            if state == 'opp':
                                from opp_dim import main as opp_main
                                result = sec_main_opp(screen, player, enemy, end)
                            elif state == 'norm':
                                from norm_dim import main as norm_main
                                result = sec_main_norm(screen, player, enemy, end)
                            elif state == 'pause':
                                ps = pause(screen)
                                if ps == 'menu':
                                    return main()
                                elif ps == False:
                                    running = False
                                    break
                                elif ps == 'norm':
                                    result = (screen, player, enemy, end, 'norm')
                            elif state == 'menu':
                                return main()

                            if not result:
                                running = False
                                break

                            screen, player, enemy, end, state = result
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if exit.is_clicked(event.pos):
                        running = False
                    elif play.is_clicked(event.pos):
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
                            elif state == 'norm':
                                from norm_dim import main as norm_main
                                result = norm_main(screen, player, box, button, end)
                            elif state == 'pause':
                                ps = pause(screen)
                                if ps == 'menu':
                                    return main()
                                elif ps == False:
                                    running = False
                                    break
                                elif ps == 'norm':
                                    result = (screen, player, box, button, end, 'norm')
                            elif state == 'menu':
                                return main()

                            if not result:
                                running = False
                                break

                            screen, player, box, button, end, state = result
                    

        screen.fill((0, 0, 0))
        
        play.draw(screen, (0, 128, 0))
        exit.draw(screen, (128, 0, 0))
        screen.blit(norm_text, (375, 260))
        screen.blit(exit_txt, (375, 365))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()