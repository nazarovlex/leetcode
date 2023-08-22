from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt_text = Counter(text)
        cnt_ball = Counter("balloon")
        max_bal = 2 ** 32
        for k, v in cnt_ball.items():
            if cnt_text[k] >= v:
                max_bal = min(max_bal, cnt_text[k] // v)
            else:
                return 0

        return max_bal


text = "loonbalxballpoon"
result = Solution().maxNumberOfBalloons(text)
print(result)
