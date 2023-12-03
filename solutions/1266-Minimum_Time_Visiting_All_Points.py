class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        return sum([ abs(points[x][0] - points[x + 1][0]) + abs(points[x][1] - points[x + 1][1]) - min(abs(points[x][0] - points[x + 1][0]), abs(points[x][1] - points[x + 1][1])) for x in range(len(points) - 1)])