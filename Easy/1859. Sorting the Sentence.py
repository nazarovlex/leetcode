class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        s.sort(key=lambda x: x[-1])
        res = ""
        for letter in s:
            res += letter[:-1] + " "
        return res[:-1]


s = "is2 sentence4 This1 a3"
result = Solution().sortSentence(s)
print(result)
