from typing import List


class Solution:  # solution #1
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_sustrings = [0]
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zero_sustrings[-1] += 1
            elif nums[i] != 0 and zero_sustrings[-1] != 0:
                zero_sustrings.append(0)

            i += 1

        def count_zero(number):
            if number <= 1:
                return number
            return count_zero(number - 1) + number

        res = 0
        for num in zero_sustrings:
            res += count_zero(num)
        return res


class Solution2:  # solution #1 faster and less memory then 1st solution
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def count_zero(number):
            if number <= 1:
                return number
            return count_zero(number - 1) + number

        cnt, res = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            elif nums[i] != 0 and cnt != 0:
                res += count_zero(cnt)
                cnt = 0

        if cnt != 0:
            res += count_zero(cnt)
        return res


class Solution3:  # solution #3 without recursion
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt, res = 0, 0
        for i in range(len(nums)):
            if nums[i]==0:
                cnt += 1
            else:
                cnt = 0
            res += cnt
        return res


# n = [1, 3, 0, 0, 2, 0, 0, 4]
n = [0, 0, 0, 2, 0, 0]
# n = [0, 0, 0]

result = Solution3().zeroFilledSubarray(n)
print(result)
