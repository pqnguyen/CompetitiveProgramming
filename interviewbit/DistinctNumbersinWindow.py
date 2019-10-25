from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        count = 0
        res = []
        tb = defaultdict(int)
        for i in range(len(A)):
            if i >= B:
                tb[A[i - B]] -= 1
                if tb[A[i - B]] == 0:
                    count -= 1
            if tb[A[i]] == 0: count += 1
            tb[A[i]] += 1
            if i >= B - 1: res.append(count)
        return res


A = [1, 2, 1, 3, 3, 3]
res = Solution().dNums(A, 0)
print(res)
