class Solution:
    def maxScore(self, s: str) -> int:
        score = 0

        curr = { '0': 0, '1': 0 }
        total = sum(map(int, list(s)))

        for i in range(len(s) - 1):
            curr[s[i]] += 1

            left = curr['0']
            right = total - curr['1']

            score = max(score, left + right)

        return score