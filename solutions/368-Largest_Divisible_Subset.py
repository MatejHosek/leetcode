class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        potencial = [ [x] for x in nums ]

        for i in range(1, len(nums)):
            maximum = []
            for j in range(0, i):
                if (nums[j]/nums[i]).is_integer() and len(potencial[j]) > len(maximum):
                    maximum = potencial[j]

            potencial[i] += maximum

        longest = []
        for p in potencial:
            if len(p) > len(longest):
                longest = p
        return longest