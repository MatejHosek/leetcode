class Solution:
    def reverse(self, x: int) -> int:
        num = 0

        if x < 0:
            num = int(str(x)[1:][::-1]) * -1
        else:
            num = int(str(x)[::-1])

        if num > -2**31 and num < 2**31 - 1:
            return num
        
        return 0