class Solution:
    def arrangeCoins(self, n: int) -> int:
        _ = 1
        while n >= _:
            n -= _
            _ += 1
        return _ - 1


n = 5
result = Solution().arrangeCoins(n)
print(result)
