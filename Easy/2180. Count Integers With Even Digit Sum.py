class Solution:
    def countEven(self, num: int) -> int:
        cnt = 0
        for i in range(1, num + 1):
            if i < 10:
                if i % 2 == 0:
                    cnt += 1
            else:
                num_sum = sum([int(x) for x in str(i)])
                if num_sum % 2 == 0:
                    cnt += 1
        return cnt


num = 30
result = Solution().countEven(num)
print(result)
