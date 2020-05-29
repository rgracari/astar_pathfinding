import pygame
import time

from map_manager import MapManager
from renderer import Renderer
from finder import Finder

def main():
    WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    pygame.display.set_caption("A* Pathfinding")
    pygame.font.init()
    screen.fill((150, 150, 150))
    
    renderer = Renderer(WIDTH_SCREEN, HEIGHT_SCREEN)

    # Initial call
    data = MapManager.load_map_from_file(1)

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    data = MapManager.load_map_from_file(1)
                elif event.key == pygame.K_KP2:
                    data = MapManager.load_map_from_file(2)
                elif event.key == pygame.K_KP3:
                    data = MapManager.load_map_from_file(3)
                elif event.key == pygame.K_KP4:
                    data = MapManager.load_map_from_file(4)
                elif event.key == pygame.K_f:
                    res = Finder.find_path_with_astar(data)
                    print(res)

        renderer.render(screen, data)
        pygame.display.flip()

main()