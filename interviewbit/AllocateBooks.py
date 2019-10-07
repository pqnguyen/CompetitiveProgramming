class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, a, m):
        if len(a) < m: return -1
        left, right = max(a), sum(a)
        res = -1
        while left <= right:
            limit = (left + right) // 2
            students = self.distribute(a, limit)
            if students > m:
                left = limit + 1
            else:
                res = limit
                right = limit - 1
        return res

    def distribute(self, a, limit):
        perstudent = nums = 0
        for pages in a:
            perstudent += pages
            if perstudent > limit:
                nums += 1
                perstudent = pages
        return nums + 1


a = [97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24]
res = Solution().books(a, 26)
print(res)
# print(Solution().distribute(a, 97))
