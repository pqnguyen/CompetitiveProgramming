import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        pq = []
        for mice in A: heapq.heappush(pq, mice)
        B.sort()
        minutes = 0
        for pos in B:
            top = heapq.heappop(pq)
            minutes = max(minutes, abs(pos - top))
        return minutes


A = [4, 0, 2]
B = [4, 0, 2]
res = Solution().mice(A, B)
print(res)
