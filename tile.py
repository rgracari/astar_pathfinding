import pygame

from constants import *

class Tile:
    def __init__(self, x, y, width, height, color, border_color, status="default"):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.border_color = border_color
        self.status = status
        self.shape = pygame.Rect(self.y, self.x, self.width, self.height)