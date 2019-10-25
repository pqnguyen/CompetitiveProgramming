from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())


res = Solution().longestArithSeqLength([24, 13, 1, 100, 0, 94, 3, 0, 3])
print(res)
