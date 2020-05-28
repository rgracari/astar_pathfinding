import pygame

from control_panel import ControlPanel
from game import Game

class WindowController:
    def __init__(self, game_width, game_height, control_panel_width, control_panel_height):
        self.game = Game()
        # self.control_panel = ControlPanel(game_width, 0, control_panel_width, control_panel_height)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    game.draw_path()
                elif event.key == pygame.K_r:
                    self.game.set_random_game()
                elif event.key == pygame.K_UP:
                    self.game.draw_one_step_forward_path()
                elif event.key == pygame.K_DOWN:
                    self.game.draw_one_step_backward_path()
        return True

    def render(self, screen):
        self.game.render(screen)
        # self.control_panel.render(screen)
