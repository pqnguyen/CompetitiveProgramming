class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, n):
        res = []
        self.generateParenthesisHelper(n, 0, "", res)
        res.sort()
        return res

    def generateParenthesisHelper(self, open, close, current, res):
        if open == close == 0:
            res.append(current)
            return

        if open: self.generateParenthesisHelper(open - 1, close + 1, current + '(', res)
        if close: self.generateParenthesisHelper(open, close - 1, current + ')', res)


res = Solution().generateParenthesis(3)
print(res)
