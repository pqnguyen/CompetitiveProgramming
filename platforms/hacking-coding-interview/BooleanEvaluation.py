# Cracking the coding interview - 8.14
# Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true),
# & (AND), I (OR), and A(XOR), and a desired boolean result value result, implement a function
# to count the number of ways of parenthesizing the expression such that it evaluates to result.The
# expression should be fully parenthesized(e.g.,(e)A(1» but not extraneously(e.g.,(((e» A(1)».
from collections import defaultdict


class Solution:
    def count_eval(self, s, result):
        dp = defaultdict(int)
        res = self.count_eval_util(s, result, dp)
        print(res)

    def count_eval_util(self, s, result, dp):
        if len(s) == 0: return 0
        if len(s) == 1: return 1 if self.string_to_bool(s) == result else 0
        key = 'true' + s if result else 'false' + s
        if key in dp: return dp[key]

        ways = 0
        for i in range(1, len(s), 2):
            ch = s[i]
            left, right = s[:i], s[i + 1:]
            left_true = self.count_eval_util(left, True, dp)
            left_false = self.count_eval_util(left, False, dp)
            right_true = self.count_eval_util(right, True, dp)
            right_false = self.count_eval_util(right, False, dp)

            total = (left_true + left_false) * (right_true + right_false)
            ways_true = 0
            if ch == '&':
                ways_true = left_true * right_true
            elif ch == '|':
                ways_true = left_true * right_true \
                            + left_false * right_true \
                            + left_true * right_false
            elif ch == '^':
                ways_true = left_true * right_false \
                            + left_false * right_true

            ways += ways_true if result else total - ways_true
        dp[key] = ways
        return ways

    def string_to_bool(self, ch):
        return True if ch == '1' else False


Solution().count_eval('1^0|0|1', False)
Solution().count_eval('0&0&0&1^1|0', True)
