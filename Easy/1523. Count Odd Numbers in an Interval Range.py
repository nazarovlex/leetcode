class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 1:
            high += 1
        if low % 2 == 1:
            low -= 1
        return (high-low)//2


low = 1
high = 9
result = Solution().countOdds(low, high)
print(result)
