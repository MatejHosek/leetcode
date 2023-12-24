class Solution:
    def minOperations(self, s: str) -> int:
        correct = [0, 0]

        for i in range(len(s)):
            if int(s[i]) == i % 2:
                correct[0] += 1
                continue

            correct[1] += 1

        return len(s) - max(correct)
