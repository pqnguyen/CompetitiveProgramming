class Solution:
    def longestValidParentheses(self, s: str) -> int:
        reverses = list(reversed(s))
        for i in range(len(reverses)): reverses[i] = '(' if reverses[i] == ')' else ')'
        reverses = "".join(reverses)
        return max(self.helper(s), self.helper(reverses))

    def helper(self, s):
        res = 0
        count = start = 0
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                res = max(res, i - start + 1)
            if count < 0:
                start = i + 1
                count = 0
        return res


res = Solution().longestValidParentheses(")()())")
print(res)
