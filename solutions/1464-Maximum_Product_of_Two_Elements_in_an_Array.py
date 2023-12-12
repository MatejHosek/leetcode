class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = max(nums)
        nums.pop(nums.index(i))
        j = max(nums)

        return (i - 1)*(j - 1)
