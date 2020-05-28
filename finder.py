class Finder:

    @staticmethod
    def find_path_static(grid, start, finish):
        path = []
        current = [start[0], start[1]]
        path.append(start)
        while current != finish:
            if current[0] < finish[0]:
                current[0] += 1
            elif current[0] > finish[0]:
                current[0] -= 1
            elif current[1] < finish[1]:
                current[1] += 1
            elif current[1] > finish[1]:
                current[1] -= 1
            path.append([current[0], current[1]])
        return path
    
    @staticmethod
    def find_path_astar():
        pass
