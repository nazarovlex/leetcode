class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        tmp_1 = 1
        tmp_2 = 0
        while n > 0:
            tmp_1 = tmp_1 * (n % 10)
            tmp_2 += n % 10
            n //= 10
        return tmp_1 - tmp_2


n = 234
result = Solution().subtractProductAndSum(n)
print(result)
