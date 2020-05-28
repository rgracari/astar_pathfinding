import constants
from grid_tile import GridTile

class Game:
    def __init__(self, tiles_witdh, tiles_height, start, finish):
        self.start = start
        self.finish = finish
        self.grid_tile = GridTile(tiles_witdh, tiles_height)
        self.set_game()

    def find_path(self):
        pass

    def set_game(self):
        self.grid_tile.updateTile(self.start[0], self.start[1], constants.TILE_STATUS_START)
        self.grid_tile.updateTile(self.finish[0], self.finish[1], constants.TILE_STATUS_FINISH)

    def render(self, screen):
        self.grid_tile.render(screen)


# # Set the player
# player_pos = [0, 0]
# grid_tile.updateTile(player_pos[0], player_pos[1], constants.TILE_STATUS_ACTIVE)


