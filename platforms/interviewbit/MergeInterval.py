# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from collections import deque


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        start, end = new_interval.start, new_interval.end
        left, right = 0, 0
        while right < len(intervals):
            if start <= intervals[right].end:
                if end < intervals[right].start:
                    break
                else:
                    start = min(start, intervals[right].start)
                    end = max(end, intervals[right].end)
            else:
                left += 1
            right += 1
        return intervals[:left] + [Interval(start, end)] + intervals[right:]
