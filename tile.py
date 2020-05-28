import pygame

import constants

class Tile:
    def __init__(self, x, y, width, height, status=constants.TILE_STATUS_DEFAULT):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = constants.GREEN
        self.border_color = constants.GREY
        self.status = status
        self.shape = pygame.Rect(self.y, self.x, self.width, self.height)
    
    def setActive(self, status):
        if status == constants.TILE_STATUS_ACTIVE:
            self.status = constants.TILE_STATUS_ACTIVE
            self.color = constants.RED
        # elif status == constants.TILE_STATUS_CURRENT:
        #     self.status = constants.TILE_STATUS_CURRENT
        #     self.color = constants.BLUE
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.shape)
        pygame.draw.rect(screen, self.border_color, self.shape, constants.TILE_BORDER_SIZE)
