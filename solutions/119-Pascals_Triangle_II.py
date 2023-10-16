import math

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = []

        for i in range(rowIndex + 1):
            row.append(self.getValue(rowIndex, i))

        return row

    def getValue(self, row: int, column: int) -> int:
        top = 1
        for i in range(column):
            top *= row - i

        bottom = math.factorial(column)

        return int(top/bottom)