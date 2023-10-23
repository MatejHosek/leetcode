class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math

        rootFour = math.sqrt(math.sqrt(n))
        if rootFour == int(rootFour):
            return True
        
        return False