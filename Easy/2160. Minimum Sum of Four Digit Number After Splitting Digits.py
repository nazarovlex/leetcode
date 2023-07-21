class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num))
        return int(num[0] + num[3]) + int(num[1] + num[2])


num = 2932
result = Solution().minimumSum(num)
print(result)
