class Solution:
    def fib(self, n: int) -> int:
        def helper(num):
            if num < 2:
                return num
            return helper(num - 1) + helper(num - 2)

        return helper(n)


class Solution2:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


n = 20
result = Solution2().fib(n)
print(result)
