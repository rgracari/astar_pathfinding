import pygame

import constants

class Tile:
    def __init__(self, y, x, width, height, status):
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.status = status
        self.color = Tile.define_color_by_status(self.status)
        self.shape = pygame.Rect(self.y, self.x, self.width, self.height)

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
        else:
            return constants.LIGHT_GREY