class Solution(object):
    ## solution #1
    # def mySqrt(self, x):
    #     i = 0
    #     while True:
    #         if i*i==x or (i+1)*(i+1)>x:
    #             return i
    #         i += 1

    ## solution #2
    def mySqrt(self, x):
        i = x // 2
        c = 0
        while True:
            if x == 0:
                return 0
            elif 0 < x < 4:
                return 1

            if i * i > x:
                c = i
                i = i // 2

            elif (i + 1) * (i + 1) < x:
                i = i + (c - i) // 2
            elif i * i == x or i * i < x < (i + 1) * (i + 1):
                return i
            elif (i + 1) * (i + 1) == x:
                return i + 1


number = 2147395599
result = Solution().mySqrt(number)
print(result)
