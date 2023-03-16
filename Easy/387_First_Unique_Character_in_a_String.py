class Solution(object):
    def firstUniqChar(self, s):
        for ind in range(len(s)):
            if s.count(s[ind])==1:
                return ind
        return -1



string = "loveleetcode"
result = Solution().firstUniqChar(string)
print(result)