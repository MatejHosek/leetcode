class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        cleanS = []; cleanT = []

        for char in s:
            if char == '#':
                if len(cleanS) > 0:
                    cleanS.pop()
                continue
            cleanS += char

        for char in t:
            if char == '#':
                if len(cleanT) > 0:
                    cleanT.pop()
                continue
            cleanT += char

        return cleanS == cleanT