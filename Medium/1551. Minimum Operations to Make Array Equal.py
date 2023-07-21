class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2 * i) + 1 for i in range(n)]

        if len(arr) % 2 == 1:
            middle = arr[len(arr) // 2]
        else:
            m1 = arr[len(arr) // 2 - 1]
            m2 = arr[len(arr) // 2]
            middle = (m1 + m2) // 2
        res = 0
        for i in range(len(arr) // 2):
            res += middle - arr[i]
        return res


n = 6
result = Solution().minOperations(n)
print(result)
