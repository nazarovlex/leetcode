class Solution(object):
    def firstBadVersion(self, n, bad):
        def isBadVersion(x):
            if x >= bad:
                return True
            return False

        if n <= 1:
            return n

        l = 0
        c = n // 2
        while True:
            if isBadVersion(c) and not isBadVersion(c - 1):
                return c
            elif isBadVersion(c) and isBadVersion(c - 1):
                c = l + (c - l) // 2
            elif not isBadVersion(c):
                l = c
                if (n - c) // 2 > 0:
                    c = (n - c) // 2 + c
                else:
                    c = (n - c) // 2 + c + 1


testcase = {5: 4, 1: 1, 2: 2, 2126753390: 1702766719}
for k, v in testcase.items():
    result = Solution().firstBadVersion(k, v)
    print(result)
