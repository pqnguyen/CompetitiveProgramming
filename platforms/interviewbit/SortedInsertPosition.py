class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchInsert(self, a, target):
        left = self.lower_bound(a, target)
        return left

    def lower_bound(self, a, target):
        left, right = 0, len(a) - 1
        res = len(a)
        while left <= right:
            mid = (left + right) // 2
            if a[mid] < target:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res


res = Solution().searchInsert([1, 2, 3], 4)
print(res)
