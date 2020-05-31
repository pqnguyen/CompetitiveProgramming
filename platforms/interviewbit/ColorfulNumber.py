class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        a = str(A)
        tb = {}
        for l in range(1, len(a) + 1):
            for i in range(len(a) - l + 1):
                j = i + l
                total = self.product(int(a[k]) for k in range(i, j))
                if total in tb: return False
                tb[total] = True

        return True

    def product(self, a):
        res = 1
        for num in a: res *= num
        return res


res = Solution().colorful(12)
print(res)
