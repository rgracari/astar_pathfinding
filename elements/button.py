import pygame

class Button:
    def __init__(self, text, x, y, height, width, color):
        self.text = text
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        # mouse_pos = pygame.mouse.get_pos()
        pass
        