class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        while x[0] == "0" and len(x) > 1:
            x = x[1:]
        if x[-1] == "-":
            x = "-" + x[:-1]
        x = int(x)
        if 2 ** 31 < x or x < -2 ** 31:
            return 0
        else:
            return x


number = -177
result = Solution().reverse(number)
print(result)
