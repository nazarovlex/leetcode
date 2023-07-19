class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stones.count(i) for i in jewels)


jewels = "aA"
stones = "aAAbbbb"
result = Solution().numJewelsInStones(jewels,stones)
print(result)
