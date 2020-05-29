import constants

class Finder:

    @staticmethod
    def find_path_static(data):
        pass
        # Finder.find_next_path(data)

    @staticmethod
    def find_next_path_static(data):
        isEnd = False
        height = len(data)
        width = len(data[0])

        current = Finder.find_item_by_status(data, constants.STATUS_START, height, width)
        finish = Finder.find_item_by_status(data, constants.STATUS_FINISH, height, width)

        if current == finish:
            isEnd = True
            return [], isEnd
        elif current[0] < finish[0]:
            current[0] += 1
        elif current[0] > finish[0]:
            current[0] -= 1
        elif current[1] < finish[1]:
            current[1] += 1
        elif current[1] > finish[1]:
            current[1] -= 1
        
        return [[current[0], current[1]]], isEnd


    @staticmethod
    def find_item_by_status(data, item_status, height, width):
        for x in range(0, height):
            for y in range(0, width):
                if item_status == data[x][y]:
                    return [x, y]