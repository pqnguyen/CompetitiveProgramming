# 1064 - Fixed Point
class Solution:
    def findFixedPoint(self, a):
        return self.findFixedPointBinarySearch(a, 0, len(a) - 1)

    def findFixedPointBinarySearch(self, a, begin, end):
        if begin > end: return -1
        mid = (begin + end) // 2
        if a[mid] == mid: return mid

        left = self.findFixedPointBinarySearch(a, begin, min(mid - 1, a[mid]))
        if left != -1:
            return left

        right = self.findFixedPointBinarySearch(a, max(mid + 1, a[mid]), end)
        if right != -1:
            return right
        return -1


res = Solution().findFixedPoint([-2, -1, 0, 5, 7, 7, 7, 8, 9, 10, 10])
print(res)
