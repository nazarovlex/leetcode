from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hash_table = {}
        for dom in dominoes:
            if (sorted(dom)[0], sorted(dom)[1]) in hash_table:
                hash_table[(sorted(dom)[0], sorted(dom)[1])] += 1
            else:
                hash_table[(sorted(dom)[0], sorted(dom)[1])] = 1
        cnt = 0
        for v in hash_table.values():
            if v > 1:
                cnt += v * (v - 1) // 2

        return cnt


dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
result = Solution().numEquivDominoPairs(dominoes)
print(result)
