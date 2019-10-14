class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        count = 0
        for start in range(len(A)):
            if A[start] > C: continue
            total = 0
            end = start
            while end < len(A) and total + A[end] <= C:
                total += A[end]
                if B <= total <= C: count += 1
                end += 1
        return count


A = [80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90]
res = Solution().numRange(A, 99, 269)
print(res)
