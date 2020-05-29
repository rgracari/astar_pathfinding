import pygame

from map_loader import MapLoader
from renderer import Renderer

def main():
    WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    pygame.display.set_caption("A* Pathfinding")
    pygame.font.init()
    screen.fill((150, 150, 150))
    
    renderer = Renderer(WIDTH_SCREEN, HEIGHT_SCREEN)

    # Initial call
    data = MapLoader.load_map_from_file(1)
    print(data)

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    data = MapLoader.load_map_from_file(1)
                elif event.key == pygame.K_KP2:
                    data = MapLoader.load_map_from_file(2)
                elif event.key == pygame.K_KP3:
                    data = MapLoader.load_map_from_file(3)
        renderer.render(screen, data)
        pygame.display.flip()

main()