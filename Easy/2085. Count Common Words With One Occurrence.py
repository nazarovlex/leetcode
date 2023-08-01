from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = Counter(words1)
        words2 = Counter(words2)
        return len({w for w, v in words1.items() if v == 1} & {w for w, v in words2.items() if v == 1})


words1 = ["leetcode", "is", "amazing", "as", "is"]
words2 = ["amazing", "leetcode", "is"]

result = Solution().countWords(words1, words2)
print(result)
