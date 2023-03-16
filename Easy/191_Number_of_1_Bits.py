class Solution(object):
    def hammingWeight(self, n):
        n = str((bin(n)))
        return n.count("1")


number = 11
result = Solution().hammingWeight(number)
print(result)
