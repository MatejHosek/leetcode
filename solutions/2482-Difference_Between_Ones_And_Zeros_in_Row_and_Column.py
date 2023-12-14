class Solution:
    def onesMinusZeros(self, matrix: List[List[int]]) -> List[List[int]]:
        onesRows = [ sum(x) for x in matrix ]
        onesCols = [ sum(x) for x in list(zip(*matrix)) ]

        zerosRows = [ len(matrix) - onesRows[i] for i in range(len(onesRows)) ]
        zerosCols = [ len(matrix[0]) - onesCols[i] for i in range(len(onesCols)) ]

        return [[ onesRows[i] + onesCols[j] - zerosRows[i] - zerosCols[j] for j in range(len(onesCols)) ] for i in range(len(onesRows)) ]