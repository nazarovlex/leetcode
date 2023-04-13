from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        tmp = []
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(tmp)
            tmp = []
        return res


result = Solution().generate(numRows=5)
print(result)
