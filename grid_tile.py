import pygame

from tile import Tile
import constants

class GridTile:
    def __init__(self, nbTilesWidth, nbTilesHeight):
        self.nbTilesWidth = nbTilesWidth
        self.nbTilesHeight = nbTilesHeight
        self.tiles = [[0 for x in range(self.nbTilesWidth)] for y in range(self.nbTilesHeight)]
        self.generateTiles()

    def generateTiles(self):
        for x in range(0, self.nbTilesHeight):
            for y in range(0, self.nbTilesWidth):
                self.tiles[x][y] = Tile(y * constants.SCREEN_WIDTH // constants.TILES_NUMBER,
                                        x * constants.SCREEN_HEIGHT // constants.TILES_NUMBER,
                                        constants.SCREEN_WIDTH // constants.TILES_NUMBER,
                                        constants.SCREEN_HEIGHT // constants.TILES_NUMBER)

    def render(self, screen):
        for line in range(0, len(self.tiles)):
            for tile in self.tiles[line]:
                tile.render(screen)

    def updateTile(self, x, y, status):
        self.tiles[x][y].setActive(status)