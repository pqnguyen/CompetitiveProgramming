import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]):
        intervals.sort(key=lambda interval: interval[0])
        heap = []
        for start, finish in intervals:
            if not heap or heap[0] > start:
                heapq.heappush(heap, finish)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, finish)
        return len(heap)


res = Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20], [4, 9], [10, 12]])
print(res)
