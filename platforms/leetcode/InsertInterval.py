from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insertedIndex = len(intervals)
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                insertedIndex = i
                break
        intervals.insert(insertedIndex, newInterval)
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                mergedIntervals = self.merge(stack.pop(), interval)
                stack.extend(mergedIntervals)
        return stack

    def merge(self, a, b):
        if b[0] <= a[1]:
            return [[min(a[0], b[0]), max(a[1], b[1])]]
        return [a, b]


res = Solution().insert([[1, 5]], [2, 7])
print(res)
