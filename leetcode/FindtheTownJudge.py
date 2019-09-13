# https://leetcode.com/problems/find-the-town-judge/


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        incommingEdges = [0] * N
        for edge in trust:
            incommingEdges[edge[1] - 1] += 1
            incommingEdges[edge[0] - 1] -= 1
        res = [-1, 0]
        for i in range(N):
            if incommingEdges[i] == N - 1:
                res[0] = i + 1
                res[1] += 1
        if res[1] == 1:
            return res[0]
        return -1
