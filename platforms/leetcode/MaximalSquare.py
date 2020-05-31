from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[1 if ele == '1' else 0 for ele in row] for row in matrix]
        length = 0
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0 and memo[i][j] == 1:
                    memo[i][j] = 1 + min(memo[i - 1][j], memo[i - 1][j - 1], memo[i][j - 1])
                if memo[i][j] > length: length = memo[i][j]
        return length ** 2


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
res = Solution().maximalSquare(matrix)
print(res)
