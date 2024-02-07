class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for a in s:
            if a not in counts.keys():
                counts[a] = 0

            counts[a] += 1
        
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        toReturn = ''

        for a, c in counts:
            toReturn += a * c

        return toReturn