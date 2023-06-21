class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        dict = {}
        for i in range(len(indices)):
            dict[indices[i]] = s[i]
        res = ""
        for i in range(len(s)):
            res += dict[i]
        return res


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
result = Solution().restoreString(s, indices)
print(result)
