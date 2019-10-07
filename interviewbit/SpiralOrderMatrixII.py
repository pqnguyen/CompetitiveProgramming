class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, n):
        if not n: return [[]]
        a = [[0] * n for _ in range(n)]
        top, bottom = 0, n
        left, right = 0, n
        count = 1
        while True:
            if left > right: break
            for i in range(left, right):
                a[top][i] = count
                count += 1
            top += 1

            if top > bottom: break
            for i in range(top, bottom):
                a[i][right - 1] = count
                count += 1
            right -= 1

            if left > right: break
            for i in range(right - 1, left - 1, -1):
                a[bottom - 1][i] = count
                count += 1
            bottom -= 1

            if top > bottom: break
            for i in range(bottom - 1, top - 1, -1):
                a[i][left] = count
                count += 1
            left += 1
        return a


res = Solution().generateMatrix(1)
print(res)
