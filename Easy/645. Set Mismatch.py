from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        res = []
        for k, v in hash.items():
            if v == 2:
                res.append(k)
                break
        for cnt in range(1, len(nums) + 1):
            if cnt not in hash:
                res.append(cnt)
                break
        return res


nums = [3, 2, 3, 4, 6, 5]
result = Solution().findErrorNums(nums)
print(result)
