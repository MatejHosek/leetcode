class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        for i in range(n // 7):
            money += 28 + i * 7

        for j in range(n % 7):
            money += n // 7 + j + 1

        return money