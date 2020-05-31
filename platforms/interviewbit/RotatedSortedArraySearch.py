class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, a, target):
        left, right = 0, len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == target: return mid
            if a[right] == a[left]:
                left += 1
                continue
            if a[left] <= a[mid]:
                if a[left] <= target < a[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if a[mid] < target <= a[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


res = Solution().search([1, 3, 1, 1, 1], 1)
print(res)
