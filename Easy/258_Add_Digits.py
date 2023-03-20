class Solution1:
    def addDigits(self, num: int) -> int:
        string_num = str(num)
        num = 0
        while len(string_num) > 1:
            num = 0
            for i in string_num:
                num += int(i)
                string_num = str(num)
        return int(string_num)


class Solution2:
    def addDigits(self, num: int) -> int:

        def num_sum(number):
            array_num = []
            while number > 0:
                array_num.append(number % 10)
                number //= 10
            return sum(array_num)

        while num > 9:
            num = num_sum(num)
        return num


n = 38
result = Solution1().addDigits(n)
print(result)
