from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        tuples = [(k, v) for k, v in hash_table.items()]
        tuples.sort(key=lambda x: (-x[1], x[0]))

        return [x[0] for x in tuples[:k]]


nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
result = Solution().topKFrequent(nums, k)
print(result)
