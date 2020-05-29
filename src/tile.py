import pygame

import constants

class Tile:
    def __init__(self, y, x, width, height, status):
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont('Arial', 25)
        self.status = status
        self.color = Tile.define_color_by_status(self.status)
        self.shape = pygame.Rect(self.y, self.x, self.width, self.height)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.shape)
        pygame.draw.rect(screen, constants.TILE_BORDER_COLOR, self.shape, constants.TILE_BORDER_SIZE)
        screen.blit(self.font.render('[{}, {}]'.format(self.y // 200, self.x//200), True, constants.GREEN), (self.y + 75, self.x + 75))

    @staticmethod
    def define_color_by_status(status):
        if status == constants.STATUS_START:
            return constants.WHITE
        elif status == constants.STATUS_FINISH:
            return constants.BLACK
        elif status == constants.STATUS_BLOCK:
            return constants.BROWN
        elif status == constants.STATUS_DEFAULT:
            return constants.LIGHT_GREY
        elif status == constants.STATUS_PATH:
            return constants.RED
        else:
            return constants.LIGHT_GREY