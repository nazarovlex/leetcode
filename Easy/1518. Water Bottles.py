class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        emptyBottles = 0
        while numBottles > 0:
            res += numBottles
            numBottles += emptyBottles
            emptyBottles = numBottles % numExchange
            numBottles = numBottles // numExchange

        return res


numBottles = 15
numExchange = 8
result = Solution().numWaterBottles(numBottles, numExchange)
print(result)
