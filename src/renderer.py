import pygame

from tile import Tile
import constants

class Renderer:
    def __init__(self, width_screen, height_screen):
        self.width_screen = width_screen
        self.height_screen = height_screen

    def render(self, screen, data):
        tiles = self.transform_data_to_tiles(data)
        for line in tiles:
            for tile in line:
                pygame.draw.rect(screen, tile.color, tile.shape)
                pygame.draw.rect(screen, constants.TILE_BORDER_COLOR, tile.shape, constants.TILE_BORDER_SIZE)

    def transform_data_to_tiles(self, data):
        nbTileHeight = len(data) 
        nbTileWidth = len(data[0])
        tileWidth = self.width_screen // nbTileWidth
        tileHeight = self.height_screen // nbTileHeight
        tiles = [[0 for x in range(nbTileWidth)] for y in range(nbTileHeight)]
        for x in range(0, nbTileHeight):
            for y in range(0, nbTileWidth):
                tiles[x][y] = Tile(x * tileWidth,
                                  y * tileHeight,
                                  tileWidth,
                                  tileHeight,
                                  data[y][x])
        return tiles
