import pygame

import constants

class Tile:
    def __init__(self, x, y, width, height, status=constants.TILE_STATUS_DEFAULT):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = constants.LIGHT_GREY
        self.border_color = constants.GREY
        self.status = status
        self.shape = pygame.Rect(self.y, self.x, self.width, self.height)
    
    def setStatus(self, status):
        if status == constants.TILE_STATUS_DEFAULT:
            self.status = constants.TILE_STATUS_DEFAULT
            self.color = constants.LIGHT_GREY
        elif self.status == constants.TILE_STATUS_START:
            return
        elif self.status == constants.TILE_STATUS_FINISH:
            return
        elif status == constants.TILE_STATUS_BLOCK:
            self.status = constants.TILE_STATUS_BLOCK
            self.color = constants.BROWN
        elif status == constants.TILE_STATUS_ACTIVE:
            self.status = constants.TILE_STATUS_ACTIVE
            self.color = constants.RED
        elif status == constants.TILE_STATUS_START:
            self.status = constants.TILE_STATUS_START
            self.color = constants.WHITE
        elif status == constants.TILE_STATUS_FINISH:
            self.status = constants.TILE_STATUS_FINISH
            self.color = constants.BLACK
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.shape)
        pygame.draw.rect(screen, self.border_color, self.shape, constants.TILE_BORDER_SIZE)
