import pygame

from tile import Tile
from constants import *

class GridTile:
    def __init__(self, nbTilesWidth, nbTilesHeight):
        self.nbTilesWidth = nbTilesWidth
        self.nbTilesHeight = nbTilesHeight
        self.tiles = [[0 for x in range(self.nbTilesWidth)] for y in range(self.nbTilesHeight)]
        self.generateTiles()

    def generateTiles(self):
        for x in range(0, self.nbTilesHeight):
            for y in range(0, self.nbTilesWidth):
                self.tiles[x][y] = Tile(y * SCREEN_WIDTH // TILES_NUMBER, x * SCREEN_HEIGHT // TILES_NUMBER, SCREEN_WIDTH//TILES_NUMBER, SCREEN_HEIGHT//TILES_NUMBER, GREEN, GREY)
                print(y * SCREEN_WIDTH // TILES_NUMBER)

    def render(self, screen):
        for line in range(0, len(self.tiles)):
            for tile in self.tiles[line]:
                pygame.draw.rect(screen, tile.color, tile.shape)
                pygame.draw.rect(screen, tile.border_color, tile.shape, TILE_BORDER_SIZE)

    # def updateTile(self, x, y, status)