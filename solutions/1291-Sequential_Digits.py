class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        digits = len(str(low))
        number = int(''.join([ str(x) for x in range(1, digits + 1) ]))

        while number < low:
            if str(number).endswith('9'):
                return self.sequentialDigits(int('1' + '0' * digits), high)
            
            number += int('1' * digits)

        if number > high:
            return []

        return [number] + self.sequentialDigits(number + 1, high)