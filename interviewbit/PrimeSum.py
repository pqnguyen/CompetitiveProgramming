class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, n):
        primes = self.sieve(n + 1)
        for i in range(len(primes) - 1):
            for j in range(i, len(primes)):
                if primes[i] + primes[j] == n:
                    return [primes[i], primes[j]]
        return []

    def sieve(self, n):
        primes = [True] * n
        for i in range(2, n):
            if primes[i]:
                j = 2
                while i * j < n:
                    primes[i * j] = False
                    j += 1
        return [i for i in range(2, n) if primes[i]]


res = Solution().primesum(4)
print(res)
