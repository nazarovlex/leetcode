class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]
        return s

string = ["H", "a", "n", "n", "a", "h"]
result = Solution().reverseString(string)
print(result)
