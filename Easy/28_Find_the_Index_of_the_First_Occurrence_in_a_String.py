class Solution(object):
    def strStr(self, haystack, needle):
       return haystack.find(needle)

haystack = "leetcode"
needle = "leeto"

s = Solution()
result = s.strStr(haystack, needle)
print(result)
