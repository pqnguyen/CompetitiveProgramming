import heapq


class Solution:
    # @return an integer
    def nchoc(self, K, A):
        MOD = int(1e9) + 7
        pq = []
        for ele in A: self.push(pq, ele)
        res = 0
        while K:
            top = self.pop(pq)
            res = (res + top) % MOD
            self.push(pq, top // 2)
            K -= 1
        return res

    def push(self, pq, val):
        heapq.heappush(pq, -val)

    def pop(self, pq):
        return -heapq.heappop(pq)


res = Solution().nchoc(3, [6, 5])
print(res)
