class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)
        if res > 2**31-1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        else:
            return int(dividend / divisor)


d = 7
r = -3
result = Solution().divide(d, r)
print(result)
