class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        beginning = 0
        for char in s:
            beginning = t.find(char, beginning)

            if beginning == -1:
                return False

            beginning += 1
        
        return True