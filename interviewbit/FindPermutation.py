class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        if not A: return []
        res = [0] * B
        largest = B
        for i in range(len(A) - 1, -1, -1):
            if A[i] == 'I':
                res[i + 1] = largest
                largest -= 1
        for i in range(len(res)):
            if res[i] == 0:
                res[i] = largest
                largest -= 1
        return res


res = Solution().findPerm('DD', 3)
print(res)
