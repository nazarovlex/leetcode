class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(n+1):
            res.append(str(bin(i)[2:]).count("1"))
        return res

n = 2
result = Solution().countBits(n)
print(result)