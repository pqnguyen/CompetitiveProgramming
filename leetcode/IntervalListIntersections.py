from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A and not B: return []
        A.extend(B)
        A.sort(key=lambda interval: (interval[0], interval[1]))
        res = []
        last = A[0]
        for i in range(1, len(A)):
            interval = self.intersection(last, A[i])
            if interval: res.append(interval)
            last = [min(last[0], A[i][0]), max(last[1], A[i][1])]
        return res

    def intersection(self, a, b):
        if a[1] >= b[0]:
            return [b[0], min(b[1], a[1])]
        return []
