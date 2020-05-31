import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        A.sort()
        B.sort()
        pq = []
        tb = {}
        n = len(A)
        i = j = n - 1
        heapq.heappush(pq, (-A[i] - B[j], i, j))
        tb[i, j] = True
        res = []
        while len(res) < n:
            total, i, j = heapq.heappop(pq)
            res.append(-total)
            if (i - 1, j) not in tb:
                heapq.heappush(pq, (-A[i - 1] - B[j], i - 1, j))
                tb[i - 1, j] = True
            if (i, j - 1) not in tb:
                heapq.heappush(pq, (-A[i] - B[j - 1], i, j - 1))
                tb[i, j - 1] = True

        return res


A = [36, 27, -35, 43, -15, 36, 42, -1, -29, 12, -23, 40, 9, 13, -24, -10, -24, 22, -14, -39, 18, 17, -21, 32, -20, 12,
     -27, 17, -15, -21, -48, -28, 8, 19, 17, 43, 6, -39, -8, -21, 23, -29, -31, 34, -13, 48, -26, -35, 20, -37, -24, 41,
     30, 6, 23, 12, 20, 46, 31, -45, -25, 34, -23, -14, -45, -4, -21, -37, 7, -26, 45, 32, -5, -36, 17, -16, 14, -7, 0,
     37, -42, 26, 28]
B = [38, 34, -47, 1, 4, 49, -18, 10, 26, 18, -11, -38, -24, 36, 44, -11, 45, 20, -16, 28, 17, -49, 47, -48, -33, 42, 2,
     6, -49, 30, 36, -9, 15, 39, -6, -31, -10, -21, -19, -33, 47, 21, 31, 25, -41, -23, 17, 6, 47, 3, 36, 15, -44, 33,
     -31, -26, -22, 21, -18, -21, -47, -31, 20, 18, -42, -35, -10, -1, 46, -27, -32, -5, -4, 1, -29, 5, 29, 38, 14, -22,
     -9, 0, 43]
res = Solution().solve(A, B)
print(res)
