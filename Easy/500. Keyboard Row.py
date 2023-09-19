from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:

            if word[0].lower() in rows[0]:
                cur_row = 0
            elif word[0].lower() in rows[1]:
                cur_row = 1
            else:
                cur_row = 2

            if set(word.lower()).issubset(set(rows[cur_row])):
                res.append(word)

        return res


words = ["Hello", "Alaska", "Dad", "Peace"]
result = Solution().findWords(words)
print(result)
