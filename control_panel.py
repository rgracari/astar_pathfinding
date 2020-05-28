import pygame

import constants
from elements.button import Button

class ControlPanel:
    def __init__(self, base_x, base_y, width, height):
        self.x = base_x
        self.y = base_y
        self.width = width
        self.height = height

        self.button = Button("Ceci est le texte", base_x, base_y, 100, 100, constants.RED)

    def render(self, screen):
        self.button.render(screen)
        # print(mousex, mousey)
        # pygame.draw.rect(screen, constants.RED, (self.x, self.y, 100, 100))