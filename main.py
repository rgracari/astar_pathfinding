import pygame
import time

import constants
from game import Game

def eventHandler():
    pass

def update():
    pass

def render():
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption(constants.CAPTION_PROJECT)

    screen.fill(constants.GREY)

    game = Game(20, 20, [0, 0], [19, 19])

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    game.draw_path()
                elif event.key == pygame.K_f:
                    game.draw_path()

        game.render(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()