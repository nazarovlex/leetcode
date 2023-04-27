from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        mas = []
        res = []
        c = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                mas.append(nums[c:i + 1])

                c = i + 1
        mas.append(nums[c:])
        for ranges in mas:
            if len(ranges) > 1:
                res.append(str(ranges[0]) + "->" + str(ranges[-1]))
            else:
                res.append(str(ranges[0]))
        return res


nums = [0, 2, 3, 4, 6, 8, 9]
result = Solution().summaryRanges(nums)
print(result)
