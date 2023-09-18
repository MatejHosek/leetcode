class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        j = 0; strengths = []
        for row in mat:
            i = 0
            while i < len(row) and row[i] == 1:
                i += 1

            strengths.append((i, j))
            j += 1

        strengths.sort()
        toReturn = []
        for row in strengths[:k]:
            toReturn.append(row[1])

        return toReturn

print(Solution().kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 5))