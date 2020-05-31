MAX_INF = float("inf")
MIN_INF = float("-inf")


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        max_val = max(A)
        min_val = min(A)
        if n <= 2: return max_val - min_val

        max_bucket = [MIN_INF] * n
        min_bucket = [MAX_INF] * n

        gap = max(1, (max_val - min_val) // (n - 1))

        for i in range(n):
            index = min((A[i] - min_val) // gap, n - 1)
            max_bucket[index] = max(max_bucket[index], A[i])
            min_bucket[index] = min(min_bucket[index], A[i])

        res = 0
        max_prev = MAX_INF
        for i in range(n):
            if min_bucket[i] == MAX_INF: continue
            res = max(res, min_bucket[i] - max_prev)
            max_prev = max_bucket[i]

        return res


res = Solution().maximumGap([1, 10, 5])
print(res)
