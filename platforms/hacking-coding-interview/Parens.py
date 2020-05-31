# Cracking the coding interview - 8.9
# Parens: Implement an algorithm-cpp to print all valid (Le., properly opened and closed) combinations
# of n pairs of parentheses.
# EXAMPLE
# Input: 3
# Output: ((())),(()()), (()()), ()(()), ()()()


class Solution:
    def parens(self, n):
        results = []
        self.parens_util(results, n, 0, '')
        print(results)

    def parens_util(self, results, op, cl, s):
        if op == cl == 0:
            results.append(s)
            return

        for ch in ['(', ')']:
            if ch == '(' and op:
                self.parens_util(results, op - 1, cl + 1, s + '(')
            elif ch == ')' and cl:
                self.parens_util(results, op, cl - 1, s + ')')


Solution().parens(4)
