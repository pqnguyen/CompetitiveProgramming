class Solution:
    def findMissingRange(self, a, lower, upper):
        if not a or a[0] > lower:
            a.insert(0, lower - 1)
        if not a or a[-1] < upper:
            a.append(upper + 1)

        res = []
        for i in range(1, len(a)):
            if a[i] - a[i - 1] == 2:
                res.append(str(a[i - 1] + 1))
            elif a[i] - a[i - 1] > 2:
                res.append("{}->{}".format(a[i - 1] + 1, a[i] - 1))
        return res


res = Solution().findMissingRange([2, 3, 5, 50, 75], 0, 99)
print(res)
