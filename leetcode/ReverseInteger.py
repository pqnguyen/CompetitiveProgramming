# https://leetcode.com/problems/reverse-integer/
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reverse = 0
        while x:
            pop = x % 10
            x //= 10
            if reverse > INT_MAX // 10 or (reverse == INT_MAX // 10 and pop > 7): return 0
            if reverse < INT_MIN // 10 or (reverse == INT_MIN // 10 and pop > 8): return 0
            reverse = reverse * 10 + pop
        return reverse * sign
