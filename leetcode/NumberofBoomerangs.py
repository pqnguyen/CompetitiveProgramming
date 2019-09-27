from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        count = defaultdict(int)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if i == j: continue
                d = self.d(points[i], points[j])
                res += count[i, d] * 2 + count[j, d] * 2
                count[i, d] += 1
                count[j, d] += 1
        return res

    def d(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


res = Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
print(res)
