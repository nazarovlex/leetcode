class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for ind, symbol in enumerate(s):
            if symbol.isalpha():
                res += symbol
            else:
                res += chr(ord(s[ind - 1]) + int(symbol))
        return res


s = "a1c1e1"
result = Solution().replaceDigits(s)
print(result)
