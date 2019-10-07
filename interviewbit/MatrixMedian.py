from bisect import bisect_right as upper_bound


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, a):
        m, n = len(a), len(a[0])
        mi = min(a[i][0] for i in range(m))
        mx = max(a[i][n - 1] for i in range(m))
        avg = self.findKth(a, m, n, mi, mx, (m * n + 1) // 2)
        return avg

    def findKth(self, a, m, n, mi, mx, desired):
        while mi < mx:
            mid = (mi + mx) // 2
            left = 0
            for i in range(m):
                tmp = upper_bound(a[i], mid)
                left += tmp
            if left < desired:
                mi = mid + 1
            else:
                mx = mid
        return mi


a = [[1, 3, 6],
     [2, 6, 9],
     [3, 6, 9]]

res = Solution().findMedian(a)
print(res)
