class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        events = []

        for flower in flowers:
            events.append((flower[0], -1))
            events.append((flower[1], 1))

        for i in range(len(people)):
            events.append((people[i], 0, i))

        events.sort()
        bloomingFlowers = 0
        for event in events:
            if len(event) == 2:
                bloomingFlowers -= event[1]
                continue

            people[event[2]] = bloomingFlowers
        return people

print(Solution().fullBloomFlowers(flowers = [[1,10],[3,3]], people = [3,3,2]))