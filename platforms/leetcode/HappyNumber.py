class Solution:
    def isHappy(self, n: int) -> bool:
        return self.helper(n, {})

    def helper(self, n, cache):
        if n == 1: return True
        if n in cache: return False
        cache[n] = True
        next = 0
        while n:
            next = next + (n % 10) ** 2
            n = n // 10
        return self.helper(next, cache)


res = Solution().isHappy(19)
print(res)
