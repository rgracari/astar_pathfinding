import pygame
import time

def main():
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
    TILES_NUMBER = 20
    TILE_BORDER_SIZE = 5

    # Colors
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (100, 100, 100)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("A* Pathfinding")

    screen.fill(GREY)

    # Drawing all squares
    tiles = [[0 for x in range(TILES_NUMBER)] for y in range(TILES_NUMBER)]
    for x in range(0, TILES_NUMBER):
        for y in range(0, TILES_NUMBER):
            tiles[x][y] = pygame.draw.rect(screen, GREEN, pygame.Rect(y * SCREEN_WIDTH // TILES_NUMBER, x * SCREEN_HEIGHT // TILES_NUMBER, SCREEN_WIDTH//TILES_NUMBER, SCREEN_HEIGHT//TILES_NUMBER))
            pygame.draw.rect(screen, GREY, pygame.Rect(y * SCREEN_WIDTH // TILES_NUMBER, x * SCREEN_HEIGHT // TILES_NUMBER, SCREEN_WIDTH//TILES_NUMBER, SCREEN_HEIGHT//TILES_NUMBER), TILE_BORDER_SIZE)

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        time.sleep(.500)

if __name__ == '__main__':
    main()