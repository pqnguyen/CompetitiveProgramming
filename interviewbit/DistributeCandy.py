import heapq


class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        pq = []
        for i, num in enumerate(A): heapq.heappush(pq, (num, i))
        res = [0] * n
        while pq:
            num, i = heapq.heappop(pq)
            candy = 1
            if i - 1 >= 0 and res[i - 1] and A[i - 1] < num:
                candy = max(candy, res[i - 1] + 1)
            if i + 1 < n and res[i + 1] and A[i + 1] < num:
                candy = max(candy, res[i + 1] + 1)
            res[i] = candy
        return sum(res)


A = [1, 2, 2, 2, 1]

res = Solution().candy(A)
print(res)
