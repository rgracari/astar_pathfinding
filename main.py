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

    game = Game(10, 10, (0, 0), (9, 9))

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         player_pos[0] -= 1
            #     elif event.key == pygame.K_RIGHT:
            #         player_pos[0] += 1
            #     elif event.key == pygame.K_UP:
            #         player_pos[1] -= 1
            #     elif event.key == pygame.K_DOWN:
            #         player_pos[1] += 1
            #     grid_tile.updateTile(player_pos[0], player_pos[1], constants.TILE_STATUS_ACTIVE)

        game.render(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()