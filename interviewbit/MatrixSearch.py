class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, a, target):
        m, n = len(a), len(a[0])
        row = self.findRow(a, m, n, target)
        return self.binarySearch(a[row - 1], n, target)

    def findRow(self, a, m, n, target):
        top, bottom = 0, m - 1
        res = m
        while top <= bottom:
            mid = (top + bottom) // 2
            if a[mid][0] <= target:
                top = top + 1
            else:
                res = mid
                bottom = mid - 1
        return res

    def binarySearch(self, row, n, target):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target: return True
            if row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


a = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
res = Solution().searchMatrix(a, 23)
print(res)
