s = "MCMXCIV"

roman_int = {"IV": 4, "IX": 9, "XL": 40, "XC": 90,
             "CD": 400, "CM": 900, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
sums = 0
roman_array = []
i = 0
while i < len(s):
    if i == len(s) - 1:
        roman_array.append(s[i])
    elif s[i] + s[i + 1] not in roman_int:
        roman_array.append(s[i])
    else:
        roman_array.append(s[i] + s[i + 1])
        i += 1
    i += 1

# print(roman_array)
for item in roman_array:
    sums += roman_int[item]

print(sums)
