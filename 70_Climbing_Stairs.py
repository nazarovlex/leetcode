class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        big = n // 2
        k = 1

        for i in range(1,big+1):
            k += n-(2*i)+i


        return k



n = 7
s = Solution()
k = s.climbStairs(n=n)
print(k)
