import constants
from node import Node

class Finder:

    @staticmethod
    def find_path_with_astar(data):
        print(data)

    @staticmethod
    def find_item_by_status(data, item_status, height, width):
        for x in range(0, height):
            for y in range(0, width):
                if item_status == data[x][y]:
                    return [x, y]