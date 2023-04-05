from operator import itemgetter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_table = {}
        res = []
        for word in words:
            if word in hash_table:
                hash_table[word] += 1
            else:
                hash_table[word] = 1

        tuples = [(word, cnt) for word, cnt in hash_table.items()]

        tuples.sort(key=(itemgetter(0)))
        tuples.sort(key=itemgetter(1), reverse=True)

        for _ in range(k):
            res.append(tuples[_][0])
        return res


class Solution2:  # Optimized 1st solution
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_table = {}
        for word in words:
            hash_table[word] = hash_table.get(word, 0) + 1

        tuples = [(word, f) for word, f in hash_table.items()]
        tuples.sort(key=lambda x: (-x[1], x[0]))

        return [t[0] for t in tuples[:k]]


words = ["i", "love", "leetcode", "i", "love", "coding"]

k = 3
result = Solution().topKFrequent(words, k)
print(result)
result = Solution2().topKFrequent(words, k)
print(result)
