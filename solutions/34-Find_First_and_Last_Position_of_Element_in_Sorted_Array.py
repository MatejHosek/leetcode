class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Edge cases
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        
        # Binary search for target
        start = self.binarySearch(nums, target)
        
        lowerBound = start
        while lowerBound > 0 and nums[lowerBound - 1] == target:
            lowerBound -= 1

        upperBound = start
        while upperBound < len(nums) - 1 and nums[upperBound + 1] == target:
            upperBound += 1

        return [lowerBound, upperBound]

    def binarySearch(self, nums: list[int], target: int) -> int:
        # Edge case, target is not in array nums
        if len(nums) == 1 and nums[0] != target:
            return -1

        midpoint = len(nums) // 2

        if nums[midpoint] == target:
            return midpoint
        
        span = []; offset = 0
        if nums[midpoint] > target:
            span = nums[:midpoint]
        else:
            span = nums[midpoint:]
            offset = midpoint

        index = self.binarySearch(span, target)
        if index == -1:
            return index
        
        return index + offset


print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 9))