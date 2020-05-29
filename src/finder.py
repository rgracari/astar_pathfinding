import constants
from node import Node


class Finder:
    # This is the A* Pathfinder i will implement others
    # pathfinder later
    @staticmethod
    def find_path_with_astar(data):
        height = len(data)
        width = len(data[0])

        start = Finder.find_item_by_status(
            data, constants.STATUS_START, height, width)
        end = Finder.find_item_by_status(
            data, constants.STATUS_FINISH, height, width)

        start_node = Node(None, start)
        end_node = Node(None, end)

        open_list = []
        closed_list = []

        open_list.append(start_node)

        while True:
            current_node = open_list[0]
            current_index = 0
            for index, node in enumerate(open_list):
                if current_node.f > node.f:
                    current_node = node
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            # !! to test !!
            # closed_list.append(Node(None, [1, 2]))
            # open_list.append(Node(None, [1, 2]))

            if current_node.position == end_node.position:
                path = []
                while current_node is not None:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]

            for new_position in [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                # If it is not walkable or if it is on the closed list, ignore it. Otherwise do the following.
                # c'est bien dans la zone

                # c'est ça qu'on test
                neighbour_new_position = [
                    current_node.position[0] + new_position[0], current_node.position[1] + new_position[1]]
                if neighbour_new_position[0] < 0 or neighbour_new_position[1] < 0:
                    continue
                if neighbour_new_position[0] >= len(data) or neighbour_new_position[1] >= len(data[0]):
                    continue
                # ce n'est pas un bloc
                if data[current_node.position[0] + new_position[0]][current_node.position[1] + new_position[1]] == constants.STATUS_BLOCK:
                    continue
                # si la position est dans la closed list on l'ignore
                if Finder.is_position_in_list(closed_list, neighbour_new_position) == True:
                    continue

                if Finder.is_position_in_list(open_list, neighbour_new_position) == False:
                    new_neighbour = Node(current_node, neighbour_new_position)
                    new_neighbour.g = Finder.get_distance_between_points(
                        new_neighbour.position, start)
                    new_neighbour.h = Finder.get_distance_between_points(
                        new_neighbour.position, end)
                    new_neighbour.f = new_neighbour.g + new_neighbour.h
                    open_list.append(new_neighbour)

                elif Finder.is_position_in_list(open_list, neighbour_new_position) == True:
                    node = Finder.get_node_from_position_in_list(
                        open_list, neighbour_new_position)
                    if node.g < current_node.g:
                        node.parent = current_node
                        node.g = Finder.get_distance_between_points(
                            node.position, start)
                        node.f = node.g + node.h

    @staticmethod
    def get_node_from_position_in_list(list, position):
        for node in list:
            if node.position == position:
                return node

    @staticmethod
    def is_position_in_list(list, position):
        for node in list:
            if node.position == position:
                return True
        return False

    @staticmethod
    def get_distance_between_points(a, b):
        x = abs(a[0] - b[0])
        y = abs(a[1] - b[1])

        if (x > y):
            return 14 * y + 10 * (x - y)
        return 14 * x + 10 * (y - x)

    @staticmethod
    def find_item_by_status(data, item_status, height, width):
        for x in range(0, height):
            for y in range(0, width):
                if item_status == data[x][y]:
                    return [x, y]
