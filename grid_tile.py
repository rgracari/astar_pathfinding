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
                self.tiles[x][y] = Tile(y * constants.SCREEN_WIDTH // self.nbTilesWidth,
                                        x * constants.SCREEN_HEIGHT // self.nbTilesHeight,
                                        constants.SCREEN_WIDTH // self.nbTilesWidth,
                                        constants.SCREEN_HEIGHT // self.nbTilesHeight)

    def render(self, screen):
        for line in range(0, len(self.tiles)):
            for tile in self.tiles[line]:
                tile.render(screen)

    def updateTile(self, x, y, status):
        self.tiles[x][y].setActive(status)