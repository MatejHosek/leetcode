class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = {}

        for letter in s:
            if letter not in counts.keys():
                counts[letter] = 1
                continue
            counts[letter] += 1

        for letter in t:
            if letter in counts.keys() and counts[letter] > 0:
                counts[letter] -= 1
                continue
            
            return letter

print(Solution().findTheDifference(s = "abcd", t = "abcde"))