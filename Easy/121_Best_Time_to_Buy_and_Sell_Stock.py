class Solution(object):
    def maxProfit(self, prices):
        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1

        return max_profit


p = [1, 2, 3, 4, 5, 2, 45, 2, 6, 0]
s = Solution()
result = s.maxProfit(p)
print(result)
