class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n:
            n, x = divmod(n, k)
            ans += x
        return ans


n = 34
k = 6
print(Solution().sumBase(n,k))
