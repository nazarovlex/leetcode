class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        cnt = 0
        num_str = str(num)
        for i in range(len(num_str) - k + 1):
            cur_num = int(num_str[i:i + k])
            if cur_num != 0:
                if num % cur_num == 0:
                    cnt += 1
        return cnt


num = 240
k = 2
result = Solution().divisorSubstrings(num, k)
print(result)
