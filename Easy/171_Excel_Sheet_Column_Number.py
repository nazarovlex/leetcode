class Solution(object):
    def titleToNumber(self, columnTitle):
        s = 0
        for i in range(len(columnTitle)):
            s = ord(columnTitle[i]) - ord("A") + 1 + s * 26
        return s


title = "AB"
result = Solution().titleToNumber(title)
print(result)
