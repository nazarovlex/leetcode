class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        count = 0
        i = 1
        while True:
            if i not in arr:
                count += 1
            if count == k:
                return i
            i += 1


arr = [2, 3, 4, 7, 11]
k = 5
result = Solution().findKthPositive(arr, k)
print(result)
