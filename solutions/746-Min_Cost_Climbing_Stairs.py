class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        stairCosts = [0, 0] + [float('inf')] * len(cost)

        for stair in range(2, len(cost) + 1):
            stairCosts[stair] = min(stairCosts[stair - 2] + cost[stair - 2], stairCosts[stair - 1] + cost[stair - 1])

        return stairCosts[len(cost)]