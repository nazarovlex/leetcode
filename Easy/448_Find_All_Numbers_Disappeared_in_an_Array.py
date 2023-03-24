from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        c = len(nums)
        nums = set(nums)
        res = []
        for i in range(1, c + 1):
            if i not in nums:
                res.append(i)
        return res


testcase = [[4, 3, 2, 7, 8, 2, 3, 1], [1, 1]]
for test in testcase:
    result = Solution().findDisappearedNumbers(test)
    print(result)
