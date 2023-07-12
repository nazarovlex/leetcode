class Solution:
    def generateTheString(self, n: int) -> str:
        a = "a"
        b = "b"
        res = ""
        if n % 2 == 1:
            res = a * n
        else:
            res = a*(n-1)+b
        return res

n = 4
result = Solution().generateTheString(n)
print(result)
