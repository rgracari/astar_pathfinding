from random import random

import constants

from grid_tile import GridTile
from finder import Finder

class Game:
    def __init__(self, tiles_witdh=20, tiles_height=20, start=[0, 0], finish=[19, 19]):
        self.tiles_witdh = tiles_witdh
        self.tiles_height = tiles_height
        self.start = start
        self.finish = finish
        self.grid_tile = GridTile(tiles_witdh, tiles_height)
        self.set_game()

    def find_path(self):
        self.path = Finder.find_path_static(self.grid_tile.tiles, self.start, self.finish)

    def draw_path(self):
        for step in self.path:
            self.grid_tile.updateTile(step[0], step[1], constants.TILE_STATUS_ACTIVE)
    
    def draw_one_step_forward_path(self):
        if self.path_step < len(self.path) - 2:
            self.path_step += 1
            next_tile = self.path[self.path_step]
            self.grid_tile.updateTile(next_tile[0], next_tile[1], constants.TILE_STATUS_ACTIVE)

    def draw_one_step_backward_path(self):
        if self.path_step > 0:
            current_tile = self.path[self.path_step]
            self.grid_tile.updateTile(current_tile[0], current_tile[1], constants.TILE_STATUS_DEFAULT)
            self.path_step -= 1

    def set_random_game(self):
        self.start = [round(random()*self.tiles_witdh-1), round(random()*self.tiles_height-1)]
        self.finish = [round(random()*self.tiles_witdh-1), round(random()*self.tiles_height-1)]
        self.grid_tile.clearTiles()
        self.set_game()

    def set_game(self):
        self.grid_tile.updateTile(self.start[0], self.start[1], constants.TILE_STATUS_START)
        self.grid_tile.updateTile(self.finish[0], self.finish[1], constants.TILE_STATUS_FINISH)
        self.path = []
        self.path_step = 0
        self.find_path()

    def render(self, screen):
        self.grid_tile.render(screen)


# # Set the player
# player_pos = [0, 0]
# grid_tile.updateTile(player_pos[0], player_pos[1], constants.TILE_STATUS_ACTIVE)


