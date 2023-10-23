class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        stairCosts = [0, 0] + [float('inf')] * len(cost)

        for stair in range(len(cost)):
            stairCosts[stair + 1] = min(stairCosts[stair] + cost[stair], stairCosts[stair + 1])
            stairCosts[stair + 2] = min(stairCosts[stair] + cost[stair], stairCosts[stair + 2])

        return stairCosts[len(cost)]