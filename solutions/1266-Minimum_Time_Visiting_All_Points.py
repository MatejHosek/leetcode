class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        distance = 0

        for x in range(len(points) - 1):
            distance += abs(points[x][0] - points[x + 1][0]) + abs(points[x][1] - points[x + 1][1]) - min(abs(points[x][0] - points[x + 1][0]), abs(points[x][1] - points[x + 1][1]))

        return distance