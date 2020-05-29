import json
import os

import constants

class MapManager:

    @staticmethod
    def load_map_from_file(map_number):
        path = os.path.join("maps", "{}.txt".format(map_number))
        f = open(path, "r")
        data = json.loads(f.read())
        return data

    @staticmethod
    def write_map(data):
        pass