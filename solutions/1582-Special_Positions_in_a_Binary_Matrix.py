class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        countSpecials = 0

        for i in range(len(mat)):
            if mat[i].count(1) == 1:
                for j in range(len(mat[0])):
                    if mat[i][j] == 1 and list(zip(*mat))[j].count(1) == 1:
                        countSpecials += 1
        
            return countSpecials
