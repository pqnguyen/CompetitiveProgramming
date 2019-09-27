class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' and (i - 1 < 0 or board[i - 1][j] == '.') and (
                        j - 1 < 0 or board[i][j - 1] == '.'):
                    res += 1
        return res
