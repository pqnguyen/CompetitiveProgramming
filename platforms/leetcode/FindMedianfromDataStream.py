import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def push_max_heap(self, val):
        heapq.heappush(self.max_heap, -val)

    def pop_max_heap(self):
        return -heapq.heappop(self.max_heap)

    def push_min_heap(self, val):
        heapq.heappush(self.min_heap, val)

    def pop_min_heap(self):
        return heapq.heappop(self.min_heap)

    def addNum(self, num: int) -> None:
        self.push_max_heap(num)
        self.push_min_heap(self.pop_max_heap())
        if len(self.max_heap) < len(self.min_heap):
            self.push_max_heap(self.pop_min_heap())

    def findMedian(self) -> float:
        total = len(self.max_heap) + len(self.min_heap)
        if total % 2 == 0:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
