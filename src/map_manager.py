import json
import os

import constants

class MapManager:

    @staticmethod
    def load_map_from_file(map_number):
        path = os.path.join("..", "maps", "{}.txt".format(map_number))
        f = open(path, "r")
        data = json.loads(f.read())
        return data

    @staticmethod
    def add_path_to_map(next_steps, data):
        for step in next_steps:
            data[step[1]][step[0]] = constants.STATUS_PATH
        return data

    @staticmethod
    def write_map(data):
        pass