# Cracking the coding interview - 8.3
# Magic Index: A magic index in an array A[1. .. n-1] is defined to be an index such that A[ i]
# i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?


class Solution:
    def magic_index_distinct(self, a, start, end):
        if start > end: return -1
        mid = (start + end) // 2
        if a[mid] == mid:
            return mid
        elif a[mid] < mid:
            return self.magic_index_distinct(a, mid + 1, end)
        else:
            return self.magic_index_distinct(a, start, mid - 1)

    def magic_index_non_distinct(self, a, start, end):
        if start > end: return -1
        mid = (start + end) // 2
        if a[mid] == mid: return mid
        left = self.magic_index_non_distinct(a, start, min(mid - 1, a[mid]))
        if left >= 0: return left

        right = self.magic_index_non_distinct(a, max(mid + 1, a[mid]), end)
        return right


a = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
res = Solution().magic_index_distinct(a, 0, len(a) - 1)
print(res)

a = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
res = Solution().magic_index_non_distinct(a, 0, len(a) - 1)
print(res)
