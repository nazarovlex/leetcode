class Solution1:  # solution #1
    def intToRoman(self, num: int) -> str:
        roman_int = {"IV": 4, "IX": 9, "XL": 40, "XC": 90,
                     "CD": 400, "CM": 900, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_num = ""

        def get_key(dict, value):
            for k, v in dict.items():
                if v == value:
                    return k

        while num > 0:
            print(roman_num)
            if num - max(roman_int.values()) >= 0:
                num -= max(roman_int.values())
                roman_num += get_key(roman_int, max(roman_int.values()))
            else:
                roman_int.pop(get_key(roman_int, max(roman_int.values())))

        return roman_num



class Solution2:  # solution #2
    def intToRoman(self, num: int) -> str:
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        ints = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman_num = ""
        i = 1
        while num > 0:
            if num - ints[-i] >= 0:
                num -= ints[-i]
                roman_num += roman[-i]

            else:
                i += 1

        return roman_num

class Solution3:  # solution #3
    def intToRoman(self, num: int) -> str:
        roman_int = ['I', 1, 'IV', 4, 'V', 5, 'IX', 9, 'X', 10, 'XL', 40, 'L', 50, 'XC', 90, 'C', 100, 'CD', 400, 'D', 500, 'CM', 900, 'M', 1000]
        res = ""
        i = len(roman_int)-1
        while num > 0:
            if num - roman_int[i] >= 0:
                num -= roman_int[i]
                res += roman_int[i-1]
            else:
                i -= 2

        return res


n = 1994

result = Solution3().intToRoman(n)
print(result)
