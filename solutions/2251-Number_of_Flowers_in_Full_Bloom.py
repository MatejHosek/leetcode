class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        starts = []
        ends = []

        for flower in flowers:
            starts.append(flower[0])
            ends.append(flower[1])

        starts.sort()
        ends.sort()

        return [bisect_right(starts, visit) - bisect_left(ends, visit) for visit in people]

print(Solution().fullBloomFlowers(flowers = [[1,10],[3,3]], people = [3,3,2]))