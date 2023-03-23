class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i, j = 0, 0
        while j < len(s) and i < len(t):
            if s[j] == t[i]:
                j += 1
            i += 1
        if j == len(s):
            return True
        return False


testcase_1 = ["abc", "axc", "ab", "acb", "b"]
testcase_2 = ["ahbgdc", "ahbgdc", "baab", "ahbgdc", "abc"]

for i in range(len(testcase_1)):
    result = Solution().isSubsequence(testcase_1[i], testcase_2[i])
    print(result)
