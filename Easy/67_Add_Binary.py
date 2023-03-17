# solution #1 (SUPER DUMB!!!)
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         c = "0"
#         a, b = a[::-1], b[::-1]
#
#         while len(a) > 0 and len(b) > 0:
#             if a[0] == b[0] == str(0):
#                 c += str(0)
#                 a = a[1:]
#                 b = b[1:]
#             elif a[0] == str(1) and b[0] == str(0) and c[-1] != str(1) or a[0] == str(0) and b[0] == str(1) and c[
#                 -1] != str(1):
#                 c = c[:-1] + str(1) + str(0)
#                 a = a[1:]
#                 b = b[1:]
#             elif a[0] == str(1) and b[0] == str(0) and c[-1] == str(1) or a[0] == str(0) and b[0] == str(1) and c[
#                 -1] == str(1):
#                 c = c[:-1] + str(0) + str(1)
#                 a = a[1:]
#                 b = b[1:]
#             elif a[0] == b[0] == str(1) and c[-1] != str(1):
#                 c += str(1)
#                 a = a[1:]
#                 b = b[1:]
#             elif a[0] == b[0] == str(1) and c[-1] == str(1):
#                 c = c[:-1] + str(1) + str(1)
#                 a = a[1:]
#                 b = b[1:]
#
#         if len(a) > 0:
#             while len(a) > 0:
#                 if a[0] == c[-1] == str(0):
#                     c += str(0)
#                 elif a[0] == str(1) and c[-1] == str(0) or a[0] == str(0) and c[-1] == str(1):
#                     c = c[:-1] + str(1) + str(0)
#                 elif a[0] == c[-1] == str(1):
#                     c = c[:-1] + str(0) + str(1)
#
#                 if len(a) == 1:
#                     break
#                 else:
#                     a = a[1:]
#         elif len(b) > 0:
#             while len(b) > 0:
#                 if b[0] == c[-1] == str(0):
#                     c += str(0)
#                 elif b[0] == str(1) and c[-1] == str(0) or b[0] == str(0) and c[-1] == str(1):
#                     c = c[:-1] + str(1) + str(0)
#                 elif b[0] == c[-1] == str(1):
#                     c = c[:-1] + str(0) + str(1)
#
#                 if len(b) == 1:
#                     break
#                 else:
#                     b = b[1:]
#         if c[-1] == str(0):
#             c = c[:-1]
#
#         return c[::-1]


# solution #2 (good)
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a = int(a,2)
#         b = int(b,2)
#         a += b
#         a = (bin(a))[2:]
#         return a
# solution 2 abbreviated
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return (bin(int(a,2) + int(b,2)))[2:]

first = "110010"
second = "10111"
result = Solution().addBinary(first, second)
print(result)
