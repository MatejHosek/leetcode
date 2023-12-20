class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = float('inf'), float('inf')
        for price in prices:
            if price < min1:
                min2 = min1
                min1 = price
                continue

            if price < min2:
                min2 = price

        if min1 + min2 > money:
            return money

        return money - min1 - min2
