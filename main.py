import pygame
import time

from constants import *
from grid_tile import GridTile

def eventHandler():
    pass

def update():
    pass

def render():
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("A* Pathfinding")

    screen.fill(GREY)

    grid_tile = GridTile(TILES_NUMBER, TILES_NUMBER)
    grid_tile.render(screen)

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        # time.sleep(.500)

if __name__ == '__main__':
    main()