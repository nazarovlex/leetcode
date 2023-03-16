class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        while n > 3:
            n = n / 3
            print(n)
        if n == 3:
            return True
        else:
            return False


number = 19684
result = Solution().isPowerOfThree(number)
print(result)
