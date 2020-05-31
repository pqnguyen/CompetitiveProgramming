# https://leetcode.com/problems/available-captures-for-rook/
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook = (i, j)
        res = 0
        res += self.move(board, rook[0], rook[1], -1, 0)
        res += self.move(board, rook[0], rook[1], 1, 0)
        res += self.move(board, rook[0], rook[1], 0, -1)
        res += self.move(board, rook[0], rook[1], 0, 1)
        return res

    def move(self, board, r0, c0, r, c):
        catch = 0
        while 0 <= r0 < 8 and 0 <= c0 < 8 and board[r0][c0] != 'B':
            if board[r0][c0] == 'p':
                catch += 1
                break
            r0 += r
            c0 += c
        return catch
