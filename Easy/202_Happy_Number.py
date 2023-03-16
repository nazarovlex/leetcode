class Solution(object):
    def isHappy(self, n):
        def sum(mas):
            sum = 0
            for num in mas:
                sum += num ** 2
            return sum

        mas = []
        past_num = []
        while True:
            mas = []
            past_num.append(n)
            for i in range(len(str(n))):
                mas.append(n % 10)
                n = n // 10
            n = sum(mas)
            if n==1:
                return True
            elif n in past_num :
                return False

number = 2
result = Solution().isHappy(number)
print(result)
