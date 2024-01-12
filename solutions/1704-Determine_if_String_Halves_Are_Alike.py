class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        for C in s[:(len(s) // 2)]:
            if C in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                count += 1

        for C in s[(len(s) // 2):]:
            if C in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                count -= 1

        return count == 0
