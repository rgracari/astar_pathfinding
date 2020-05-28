import constants

from grid_tile import GridTile
from finder import Finder

class Game:
    def __init__(self, tiles_witdh, tiles_height, start, finish):
        self.start = start
        self.finish = finish
        self.grid_tile = GridTile(tiles_witdh, tiles_height)
        self.set_game()

    def find_path(self):
        return Finder.find_path_static(self.grid_tile.tiles, self.start, self.finish)

    def draw_path(self):
        path = self.find_path()
        for step in path:
            self.grid_tile.updateTile(step[0], step[1], constants.TILE_STATUS_ACTIVE)

    def set_game(self):
        self.grid_tile.updateTile(self.start[0], self.start[1], constants.TILE_STATUS_START)
        self.grid_tile.updateTile(self.finish[0], self.finish[1], constants.TILE_STATUS_FINISH)

    def render(self, screen):
        self.grid_tile.render(screen)


# # Set the player
# player_pos = [0, 0]
# grid_tile.updateTile(player_pos[0], player_pos[1], constants.TILE_STATUS_ACTIVE)


