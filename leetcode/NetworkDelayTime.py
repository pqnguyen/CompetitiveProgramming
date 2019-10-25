import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for source, desc, time in times: graph[source].append((desc, time))
        return self.dijkstra(graph, K, N)

    def dijkstra(self, graph, source, N):
        MAX_INT = 2 ** 31 - 1
        time = [MAX_INT] * (N + 1)
        time[0] = 0
        visited = [False] * (N + 1)
        pq = []
        heapq.heappush(pq, (0, source))
        time[source] = 0
        visited[source] = True
        while pq:
            d, source = heapq.heappop(pq)
            visited[source] = True
            for desc, t in graph[source]:
                if not visited[desc] and time[desc] > d + t:
                    time[desc] = d + t
                    heapq.heappush(pq, (time[desc], desc))
        maxTime = max(time)
        return -1 if maxTime == MAX_INT else maxTime


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
res = Solution().networkDelayTime(times, N, K)
print(res)
