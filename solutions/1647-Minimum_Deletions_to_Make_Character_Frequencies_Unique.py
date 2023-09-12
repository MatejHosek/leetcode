class Solution:
    def minDeletions(self, s: str) -> int:
        # Count the letters in string
        counts = {}
        for char in s:
            if char not in counts.keys():
                counts[char] = 1
                continue

            counts[char] += 1

        sortedCounts = sorted(counts.values(), reverse=True)

        # Loop through counts and decide if the value is unique
        changes = 0
        i = 1
        while i < len(sortedCounts):
            if sortedCounts[i] >= sortedCounts[i-1] and sortedCounts[i] > 0:
                sortedCounts[i] -= 1
                changes += 1
                continue

            i += 1
            return changes
