class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counts = {}
        for num in nums:
            if num not in counts.keys():
                counts[num] = 0

            counts[num] += 1

        operations = 0
        for value in counts.values():
            if value == 1:
                return -1
            
            import math
            operations += math.ceil(value / 3.0)

        return operations