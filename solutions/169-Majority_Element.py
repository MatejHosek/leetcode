class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mostCount = 0
        mostNum = 0
        
        for n in set(nums):
            if nums.count(n) > mostCount:
                mostCount = nums.count(n)
                mostNum = n

        return mostNum

print(Solution().majorityElement([3, 2, 3]))