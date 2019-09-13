# Confusing Number
class Solution:
    def confusingNumber(self, n):
        validRotated = {0, 1, 3, 6, 8, 9}
        rotatedN = 0
        oldN = n
        while n:
            digit = n % 10
            if digit not in validRotated:
                return False
            rotatedN = rotatedN * 10 + digit
            n = n // 10
        return rotatedN != oldN


res = Solution().confusingNumber(25)
print(res)
