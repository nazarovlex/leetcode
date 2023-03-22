class Solution1:
    def maxDepth(self, s: str) -> int:
        mas = []
        cnt = 0
        for i in range(len(s)):
            if s[i] == "(":
                cnt += 1
                mas.append(cnt)
            elif s[i] == ")":
                cnt -= 1
                mas.append(cnt)
            else:
                mas.append(cnt)
        return max(mas)


class Solution2: # optimized 1st solution method
    def maxDepth(self, s: str) -> int:
        cnt,res = 0,0
        for i in range(len(s)):
            if s[i] == "(":
                cnt += 1
                res = max(cnt,res)
            elif s[i] == ")":
                cnt -= 1
                res = max(cnt,res)
        return res


string = "(1+(2*3)+((8)/4))+1"
result = Solution2().maxDepth(string)
print(result)