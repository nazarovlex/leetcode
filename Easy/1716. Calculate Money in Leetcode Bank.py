class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        money = 0
        for day in range(1, n + 1):
            if day % 7 != 1:
                money += 1
                res += money
            else:
                money = 1 + (day // 7)
                res += money
        return res


n = 10
result = Solution().totalMoney(n)
print(result)
