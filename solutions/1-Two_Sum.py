class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = 0
        while index < len(nums):
            if (target - nums[index]) in nums[index+1:]:
                return [index, nums[index+1:].index(target - nums[index]) + index + 1]
            
            index += 1