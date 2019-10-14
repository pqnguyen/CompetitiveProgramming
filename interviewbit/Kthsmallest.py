class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, K):
        a = list(A)
        left, right = 0, len(a) - 1
        while left <= right:
            mid = self.partition(a, left, right)
            if mid == K - 1: return a[mid]
            if mid > K - 1:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def partition(self, a, left, right):
        wall = left
        for i in range(left, right):
            if a[i] < a[right]:
                a[wall], a[i] = a[i], a[wall]
                wall += 1
        a[wall], a[right] = a[right], a[wall]
        return wall


A = [2, 1, 4, 3, 2]
res = Solution().kthsmallest(A, 5)
print(res)
