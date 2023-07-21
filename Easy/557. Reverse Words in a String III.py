class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        res = ""
        for word in s:
            res += word[::-1] + " "
        return res[:-1]


s = "Let's take LeetCode contest"
result = Solution().reverseWords(s)
print(result)
