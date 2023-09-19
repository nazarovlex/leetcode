class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        length = max(len1, len2)
        res = ""
        for i in range(length):
            if len1 > i:
                res += word1[i]
            if len2 > i:
                res += word2[i]
        return res


w1 = "ab"
w2 = "pqrs"
result = Solution().mergeAlternately(w1, w2)
print(result)
