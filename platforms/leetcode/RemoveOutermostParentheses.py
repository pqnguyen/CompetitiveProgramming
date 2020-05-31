# https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        begin = count = 0
        for i in range(len(S)):
            if S[i] == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                res += S[begin + 1:i]
                begin = i + 1
        return res
