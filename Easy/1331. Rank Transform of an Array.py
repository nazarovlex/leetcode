from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_table = {}
        nums = sorted(arr)
        c = 1
        for num in nums:
            if num not in rank_table:
                rank_table[num] = c
            else:
                continue
            c += 1
        res = []
        for num in arr:
            res.append(rank_table[num])
        return res


arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
result = Solution().arrayRankTransform(arr)
print(result)
