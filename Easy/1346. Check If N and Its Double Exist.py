class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] == 2 * arr[j]:
                        return True

        return False


arr = [10, 2, 5, 3]
result = Solution().checkIfExist(arr)
print(result)
