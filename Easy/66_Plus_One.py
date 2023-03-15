class Solution(object):
    ## solution #1
    # def plusOne(self, digits):
    #     s = 0
    #     for n in digits:
    #         s = (s*10) + n
    #     s += 1
    #     digits = []
    #     for n in range(len(str(s))):
    #         digits.append(int(str(s)[n]))
    #     return digits

    ## solution #2
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 < 10:
                digits[i] += 1
                break
            elif i==0:
                digits.insert(0,1)
                digits[1] = 0
            elif digits[i] == 9:
                digits[i] = 0
        return digits


d = [9]
result = Solution().plusOne(d)
print(result)
