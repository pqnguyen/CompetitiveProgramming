import math


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n
        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                p = i
                while p + i < n:
                    primes[p + i] = False
                    p = p + i
        res = 0
        for i in range(2, n):
            if primes[i]: res += 1
        return res
