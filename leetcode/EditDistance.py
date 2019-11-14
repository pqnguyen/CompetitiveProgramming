class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2) + 1, len(word1) + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(n): dp[0][i] = i
        for i in range(m): dp[i][0] = i

        for i in range(1, m):
            for j in range(1, n):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[m - 1][n - 1]


word1 = "aab"
word2 = "aab"
print(Solution().minDistance(word1, word2))
