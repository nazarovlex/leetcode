from typing import List


# solution #1
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sentence in sentences:
            res = max(res, sentence.count(" ") + 1)
        return res


# solution #2
# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int:
#         return max([s.count(" ") for s in sentences]) + 1

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
result = Solution().mostWordsFound(sentences)
print(result)
