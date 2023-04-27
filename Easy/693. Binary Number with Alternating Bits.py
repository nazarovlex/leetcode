class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        for _ in range(len(n) - 1):
            if n[_] == n[_ + 1]:
                return False
        return True


n = 8
result = Solution().hasAlternatingBits(n)
print(result)
