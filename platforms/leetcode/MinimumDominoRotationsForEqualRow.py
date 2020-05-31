from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        MAX_INT = 2 ** 31 - 1

        def check(x):
            rotationA = rotationB = 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x: return MAX_INT
                if B[i] != x and A[i] == x:
                    rotationB += 1
                elif A[i] != x:
                    rotationA += 1
            return min(rotationA, rotationB)

        a = check(A[0])
        b = check(B[0])
        res = min(a, b)
        if res == MAX_INT: return -1
        return res


A = [1, 2, 1, 1, 1, 2, 2, 2]
B = [2, 1, 2, 2, 2, 2, 2, 2]
print(Solution().minDominoRotations(A, B))
