from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s[0] == s[-1]:
            return [len(s)]
        last_index = {s[i]: i for i in range(len(s))}
        res = []
        i = 0
        while i < len(s):
            end = last_index[s[i]]
            j = i + 1
            while j < end:
                if last_index[s[j]] > end:
                    end = last_index[s[j]]
                j += 1
            res.append(end - i + 1)
            i = end + 1
        return res


s = "ababcbacadefegdehijhklij"
result = Solution().partitionLabels(s)
print(result)
