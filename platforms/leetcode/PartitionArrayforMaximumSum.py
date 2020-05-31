from collections import defaultdict
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if not A: return 0
        n = len(A)
        res = defaultdict(int)
        for i in range(0, n):
            m = A[i]
            for j in range(i, max(i - K, -1), -1):
                m = max(m, A[j])
                res[i] = max(res[i], res[j - 1] + m * (i - j + 1))

        return max(res.values())