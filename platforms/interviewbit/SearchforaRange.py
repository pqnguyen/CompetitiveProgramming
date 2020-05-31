class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, a, target):
        left = self.lower_bound(a, target)
        if a[left] != target: return [-1, -1]
        right = self.upper_bound(a, target)
        return [left, right]

    def lower_bound(self, a, target):
        left, right = 0, len(a) - 1
        while left < right:
            mid = (left + right) // 2
            if a[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def upper_bound(self, a, target):
        left, right = 0, len(a) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if a[mid] > target:
                right = mid - 1
            else:
                left = mid

        return left


res = Solution().searchRange([1, 2, 3], 1)
print(res)
