import pygame

def main():
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("A* Pathfinding")

    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 80, 80))

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

if __name__ == '__main__':
    main()