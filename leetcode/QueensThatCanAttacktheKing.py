from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        grid = set()
        for queen in queens: grid.add((queen[0], queen[1]))
        for dr, dc in [(-1, -1), (1, 1), (0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]:
            self.move(grid, king, dr, dc, res)
        return res

    def move(self, grid, king, dr, dc, res):
        i, j = king
        while self.valid(i, j):
            if (i, j) in grid:
                res.append([i, j])
                break
            i += dr
            j += dc

    def valid(self, i, j):
        return 0 <= i < 8 and 0 <= j < 8


queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
king = [0, 0]
res = Solution().queensAttacktheKing(queens, king)
print(res)
