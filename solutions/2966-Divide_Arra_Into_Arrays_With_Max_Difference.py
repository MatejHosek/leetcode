class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()

        toReturn = []

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []

            toReturn.append(nums[i:i+3])

        return toReturn