import json
import os
import math

import constants

class MapManager:

    @staticmethod
    def load_map_from_file(map_number):
        path = os.path.join("..", "maps", "{}.txt".format(map_number))
        f = open(path, "r")
        data = json.loads(f.read())
        return data

    @staticmethod
    def draw_path_with_steps(map, steps):
        for x, line in enumerate(map):
            for y, letter in enumerate(line):
                if map[x][y] == constants.STATUS_PATH:
                    map[x][y] = constants.STATUS_DEFAULT
        for step in steps:
            if map[step[0]][step[1]] != constants.STATUS_START and map[step[0]][step[1]] != constants.STATUS_FINISH:
                map[step[0]][step[1]] = constants.STATUS_PATH
        return map
    
    @staticmethod
    def write_map_with_mouse_click(map, position, status):
        width = len(map[0])
        height = len(map)
        x = math.floor((position[0] * width) / 800)
        y = math.floor((position[1] * height) / 800)
        map[y][x] = status
        return map