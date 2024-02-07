class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = str(sorted(s))
            if key not in groups.keys():
                groups[key] = []

            groups[key].append(s)

        return groups.values()
