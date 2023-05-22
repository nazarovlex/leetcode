from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        res = 0
        for word in words[left:right + 1]:
            if word[0] in "aeoui":
                if word[-1] in "aeoui":
                    res += 1
        return res


w = ["hey", "aeo", "mu", "ooo", "artro"]
l = 1
r = 4
result = Solution().vowelStrings(w, l, r)
print(result)
