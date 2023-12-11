class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        number, occurence = 0, 0
        
        for i in arr:
            if i == number:
                occurence += 1
            else:
                number = i
                occurence = 1

            if occurence > 0.25 * len(arr):
                return number
