class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        newImg = [[ 0 for x in range(len(img[0])) ] for y in range(len(img))]
        for y in range(len(img)):
            for x in range(len(img[y])):
                total = 0
                cells = 0

                for n in neighbors:
                    if y + n[0] < 0 or y + n[0] >= len(img) or x + n[1] < 0 or x + n[1] >= len(img[y]):
                        continue

                    cells += 1
                    total += img[y + n[0]][x + n[1]]

                newImg[y][x] = total // cells

        return newImg
