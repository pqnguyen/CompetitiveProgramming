# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        return x == self.reverse(x)

    def reverse(self, n):
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n // 10
        return res