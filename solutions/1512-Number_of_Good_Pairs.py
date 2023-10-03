class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # n: n - 2 + n - 3 + ... + 2 + 1 = n(n - 1)/2

        counts = {}
        for num in nums:
            if num not in counts.keys():
                counts[num] = 1
                continue

            counts[num] += 1

        total = 0
        for count in counts.values():
            total += count * (count - 1) // 2

        return total

print(Solution().numIdenticalPairs([1,2,3]))