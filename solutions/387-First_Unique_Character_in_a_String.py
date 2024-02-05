class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabet = 'abcdefghijklnopqrstuvwxyz'
        first = float('inf')
        found = False

        for a in alphabet:
            if s.count(a) == 1:
                first = min(s.index(a), first)
                found = True

        if not found:
            return -1
        return first
