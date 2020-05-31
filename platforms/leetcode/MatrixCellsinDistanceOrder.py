# https://leetcode.com/problems/matrix-cells-in-distance-order/
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        allDistances = []
        for i in range(R):
            for j in range(C):
                d = self.distance(i, j, r0, c0)
                allDistances.append((i, j, d))
        allDistances.sort(key=lambda ele: ele[2])
        return [[ele[0], ele[1]] for ele in allDistances]

    def distance(self, r0, c0, r1, c1):
        return abs(r0 - r1) + abs(c0 - c1)
