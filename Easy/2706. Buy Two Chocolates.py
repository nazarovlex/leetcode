class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:

        if sum(sorted(prices)[:2]) > money:
            return money
        else:
            return money - sum(sorted(prices)[:2])


prices = [1, 2, 3]
money = 3
result = Solution().buyChoco(prices, money)
print(result)
