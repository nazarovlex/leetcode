from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        pos = operations.count("X++") + operations.count("++X")
        neg = operations.count("X--") + operations.count("--X")
        return pos - neg


operations = ["--X","X++","X++"]
result = Solution().finalValueAfterOperations(operations)
print(result)