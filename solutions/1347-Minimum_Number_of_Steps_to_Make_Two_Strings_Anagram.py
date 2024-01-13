class Solution:
    def minSteps(self, s: str, t: str) -> int:
        difference = 0
        
        for c in set(t):
            difference += max(0, t.count(c) - s.count(c))

        return difference
