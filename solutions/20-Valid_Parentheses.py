class Solution:
    def isValid(self, s: str) -> bool:
        pairs = (('(', ')'), ('[', ']'), ('{', '}'))
        path = []
        
        for char in s:
            for opening, closing in pairs:
                if char == closing:
                    if path and path[-1] == opening:
                        path.pop()
                        continue
                    return False

                if char == opening:
                    path.append(char)

        return len(path) == 0
