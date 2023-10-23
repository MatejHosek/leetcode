class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        
        if n <= 0:
            return False

        rootFour = math.log(n, 4)
        return rootFour == int(rootFour)