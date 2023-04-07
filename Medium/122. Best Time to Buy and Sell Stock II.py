from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res += prices[i + 1] - prices[i]
        return res


prices = [7, 1, 5, 3, 6, 4]
result = Solution().maxProfit(prices)
print(result)
