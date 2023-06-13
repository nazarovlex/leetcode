class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        qwe = time // (n - 1) % 2
        if qwe == 0:
            return time % (n - 1) + 1
        else:
            return n - time % (n - 1)



class Solution2:
    def passThePillow(self, n: int, time: int) -> int:
        return time % (n - 1) + 1 if time // (n - 1) % 2 == 0 else n - time % (n - 1)


n = 4
time = 5
result = Solution().passThePillow(n, time)
print(result)
result = Solution2().passThePillow(n, time)
print(result)