class Solution:
    def secondHighest(self, s: str) -> int:
        nums = sorted(set(int(x) for x in s if x.isdigit()))
        if len(nums) < 2:
            return -1
        return list(nums)[-2]


s = "sjhtz8344"
result = Solution().secondHighest(s)
print(result)
