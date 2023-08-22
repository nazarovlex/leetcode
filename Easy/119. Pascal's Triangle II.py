from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res_rows = []
        for i in range(rowIndex + 1):
            if i == 0:
                tmp_row = [1]
            else:
                tmp_row = [1]+[0] * (i - 1)+[1]
                if i > 1:
                    for j in range(1, i):
                        tmp_row[j] = res_rows[j] + res_rows[j - 1]
            res_rows = tmp_row
        return res_rows


rowIndex = 3
result = Solution().getRow(rowIndex)
print(result)
