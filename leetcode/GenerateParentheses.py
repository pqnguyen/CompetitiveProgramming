from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pattern, res = [], []
        self.generatePerenthesisUtil(n, 0, pattern, res)
        return res

    def generatePerenthesisUtil(self, open, close, pattern, res):
        if open == 0 and close == 0:
            res.append("".join(pattern))
            return

        if open:
            pattern.append('(')
            self.generatePerenthesisUtil(open - 1, close + 1, pattern, res)
            pattern.pop()

        if close:
            pattern.append(')')
            self.generatePerenthesisUtil(open, close - 1, pattern, res)
            pattern.pop()


res = Solution().generateParenthesis(3)
print(res)
