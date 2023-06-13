from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n < 11:
            return [1, n - 1]
        for i in range(1, n):
            if str(i).count("0") == 0 and str(n - i).count("0") == 0:
                return [i, n - i]


n = 1010
result = Solution().getNoZeroIntegers(n)
print(result)
