class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n == 2:
                return True
            elif n == 1:
                return True
            else:
                n = n / 2
        return False


number = 16
result = Solution().isPowerOfTwo(number)
print(result)
