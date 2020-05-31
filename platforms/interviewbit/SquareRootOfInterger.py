class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, x):
        res = 0
        lo, hi = 0, x
        for i in range(int(1e4)):
            mid = (lo + hi) // 2
            if mid * mid <= x:
                lo = mid + 1
                res = mid
            else:
                hi = mid
        return res


res = Solution().sqrt(8)
print(res)
