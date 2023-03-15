class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = []
        for i in range(1, n + 1):
            if i < 3:
                ways.append(i)
            else:
                ways.append(ways[-1] + ways[-2])

        return ways[-1]


n = 100
s = Solution()

for i in range(3, n + 1):
    k = s.climbStairs(n=i)
    print(k)
