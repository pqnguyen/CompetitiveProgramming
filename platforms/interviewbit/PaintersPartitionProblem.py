class Solution:
    def paint(self, K, T, L):
        MOD = 10000003
        L = [(l * T) % MOD for l in L]
        left, right = max(L), sum(L)
        res = 0
        while left <= right:
            limit = (left + right) // 2
            painters = self.distributePainters(L, limit)
            if painters > K:
                left = limit + 1
            else:
                res = limit
                right = limit - 1
        return res % MOD

    def distributePainters(self, L, limit):
        currentTime = painters = 0
        for time in L:
            currentTime += time
            if currentTime > limit:
                painters += 1
                currentTime = time

        return painters + 1


res = Solution().paint(10, 5, [1, 10])
print(res)
