class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        minimum = len(nums) // 3
        counts = {}; majority = []
        for num in nums:
            if num in majority:
                continue

            if num not in counts.keys():
                counts[num] = 0
            counts[num] += 1

            if counts[num] > minimum:
                majority.append(num)

        return majority
