from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_acc = 0
        for nums in accounts:
            max_acc = max(max_acc, sum(nums))
        return max_acc


accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
result = Solution().maximumWealth(accounts)
print(result)
