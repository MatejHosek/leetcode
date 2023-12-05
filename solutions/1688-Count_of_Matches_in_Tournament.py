class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            if n % 2:
                # Odd number of teams
                matches += (n - 1) / 2
                n = (n - 1) / 2 + 1
                continue
            
            # Even number of teams
            matches += n / 2
            n = n / 2

        return int(matches)