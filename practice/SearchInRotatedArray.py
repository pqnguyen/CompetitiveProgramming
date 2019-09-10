# Cracking the coding interview - 10.3
# Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.


class Solution:
    def search(self, a, target):
        pivot = self.find_pivot(a)
        if a[0] > target:
            return self.binary_search(a, target, pivot, len(a) - 1)
        else:
            return self.binary_search(a, target, 0, pivot - 1)

    def find_pivot(self, a):
        start, end = 0, len(a) - 1
        res = None
        while start <= end:
            mid = (start + end) // 2
            if a[mid] >= a[0]:
                start = mid + 1
            else:
                res = mid
                end = mid - 1
        return res

    def binary_search(self, a, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if a[mid] == target:
                return mid
            if a[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return None


a = [5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 1, 2, 3, 4]
res = Solution().search(a, 1)
print(res)
