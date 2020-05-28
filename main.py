import pygame

import constants
from window_controller import WindowController

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_WIDTH))
    pygame.display.set_caption(constants.CAPTION_PROJECT)
    pygame.font.init()
    screen.fill(constants.GREY)

    # Controller of the view
    window_controller = WindowController(constants.GAME_WIDTH,
                                         constants.GAME_WIDTH,
                                         constants.CONTROL_PANEL_WIDTH,
                                         constants.CONTROL_PANEL_HEIGHT)

    # Main Loop
    run = True
    while run:
        run = window_controller.update()
        window_controller.render(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()