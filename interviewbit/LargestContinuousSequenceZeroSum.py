class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        tb = {0: -1}
        start, end = -1, -1
        total = 0
        for i, num in enumerate(A):
            total += num
            if total in tb:
                if i - tb[total] > end - start:
                    start, end = tb[total] + 1, i + 1
            else:
                tb[total] = i
        if start != -1: return A[start: end]
        return []


res = Solution().lszero([1, 2, -3, 3])
print(res)
