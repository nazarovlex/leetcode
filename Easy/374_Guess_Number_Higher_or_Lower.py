# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import math


class Solution:
    def guessNumber(self, n: int, x) -> int:
        def guess(num):
            if num == x:
                return 0
            elif num > x:
                return -1
            elif num < x:
                return 1

        l = 0
        r = n // 2
        while True:
            if guess(r) == 0:
                return r
            elif guess(r) == -1:
                r = r - (r - l) // 2
            elif guess(r) == 1:
                l = r
                if (n - r) % 2 > 0:
                    r = r + (n - r) // 2 + 1
                else:
                    r = r + (n - r) // 2


testcase = {10: 6, 1: 1, 2: 1}
for k, v in testcase.items():
    result = Solution().guessNumber(k, v)
    print(result)
