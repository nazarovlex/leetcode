from collections import Counter
from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-zA-Z]', ' ', paragraph)
        words = paragraph.lower().split()
        counter = Counter(words)
        for word in banned:
            if word in counter:
                counter.pop(word)
        for k, v in counter.items():
            if v == max(counter.values()):
                return k


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
result = Solution().mostCommonWord(paragraph, banned)
print(result)
