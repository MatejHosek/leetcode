class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        directions = {'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1)}

        x, y = 0, 0
        for V in path:
            x += directions[V][0]
            y += directions[V][1]

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False