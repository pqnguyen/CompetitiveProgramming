MIN_INT = -2 ** 31


class Solution:
    def findSmallestCommonInAllRow(self, a):
        n = len(a)
        m = MIN_INT
        count = 0
        while True:
            for row in a:
                index = self.findAtLeast(row, m)
                if index == -1:
                    return -1
                elif row[index] == m:
                    count += 1
                else:
                    count = 1
                    m = row[index]
                if count == n:
                    return m

    def findAtLeast(self, row, val):
        left, right = 0, len(row) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] >= val:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res


a = [
    [1, 2, 2, 4, 6],
    [3, 4, 5, 8, 10],
    [3, 5, 7, 9, 11],
    [1, 3, 5, 7, 9]
]
res = Solution().findSmallestCommonInAllRow(a)
print(res)
