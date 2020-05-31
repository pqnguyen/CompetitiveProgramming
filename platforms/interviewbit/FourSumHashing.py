from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        tb = defaultdict(list)
        n = len(A)
        for i in range(n - 1):
            for j in range(i + 1, n):
                tb[A[i] + A[j]].append((i, j))

        res = []
        unique = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                total = B - A[i] - A[j]
                if total in tb:
                    for ii, jj in tb[total]:
                        if ii != i and jj != i and ii != j and jj != j:
                            a = [A[i], A[j], A[ii], A[jj]]
                            a.sort()
                            key = ":".join(str(num) for num in a)
                            if key not in unique:
                                res.append(a)
                                unique[key] = True
        res.sort()
        return res


res = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
print(res)
